__author__ = 'sunkumar'
import scipy
import numpy as np;
import pandas as pd;
import nltk as nl;
import sklearn as sk;

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("C:/Users/sunkumar/Desktop/input/Set2.txt",header=None,sep='\t')
df1 = pd.read_csv("C:/Users/sunkumar/Desktop/output/output.txt",header=None,sep='\t')
df_train = df
df_test = df1

# auth=[]
# topi=[]
# summ=[]
# word=[]
#print(df_train)
x=[]
d_x_a={}
d_x_t={}
d_x_s={}
output=[]
for i in range(0,len(df_train[3])):
    x=df_train.iloc[i][3].split(';')
    for j in x:
        if j in d_x_a.keys():
            d_x_a[j][df_train.iloc[i][1]]=d_x_a[j][df_train.iloc[i][1]]+1
        else:
            d_x_a[j]=[0,0,0]
            d_x_a[j][df_train.iloc[i][1]]=d_x_a[j][df_train.iloc[i][1]]+1
    x=df_train.iloc[i][4].split(' ')
    for j in x:
        if j in d_x_t.keys():
            d_x_t[j][df_train.iloc[i][1]]=d_x_t[j][df_train.iloc[i][1]]+1
        else:
            d_x_t[j]=[0,0,0]
            d_x_t[j][df_train.iloc[i][1]]=d_x_t[j][df_train.iloc[i][1]]+1
    x=df_train.iloc[i][5].split(' ')
    for j in x:
        if j in d_x_s.keys():
            d_x_s[j][df_train.iloc[i][1]]=d_x_s[j][df_train.iloc[i][1]]+1
        else:
            d_x_s[j]=[0,0,0]
            d_x_s[j][df_train.iloc[i][1]]=d_x_s[j][df_train.iloc[i][1]]+1
#print(d_x_a)
suc_count=0
fail_count=0

for i in range(0,len(df_test[3])):
    l=[0,0,0]
    l_max=[0,0,0]
    l1=[0,0,0]
    l_max1=[0,0,0]
    l2=[0,0,0]
    l_max2=[0,0,0]
    #p_max=[-1,-1,-1]
    p_max1=[-1,-1,-1]
    x=df_test.iloc[i][3].split(';')
    for j in x:
        if j in d_x_a.keys():
            if((d_x_a[j][0]+d_x_a[j][1]+d_x_a[j][2])!=0):
                l[0]=d_x_a[j][0]/(d_x_a[j][0]+d_x_a[j][1]+d_x_a[j][2])
                l[1]=d_x_a[j][1]/(d_x_a[j][0]+d_x_a[j][1]+d_x_a[j][2])
                l[2]=d_x_a[j][2]/(d_x_a[j][0]+d_x_a[j][1]+d_x_a[j][2])
                l_max[0]=l_max[0]+l[0]
                l_max[1]=l_max[1]+l[1]
                l_max[2]=l_max[2]+l[2]
    #p_max=max(l_max[0],l_max[1],l_max[2])
    x=df_test.iloc[i][4].split(' ')
    for j in x:
        if j in d_x_t.keys():
            if((d_x_t[j][0]+d_x_t[j][1]+d_x_t[j][2])!=0):
                l1[0]=d_x_t[j][0]/(d_x_t[j][0]+d_x_t[j][1]+d_x_t[j][2])
                l1[1]=d_x_t[j][1]/(d_x_t[j][0]+d_x_t[j][1]+d_x_t[j][2])
                l1[2]=d_x_t[j][2]/(d_x_t[j][0]+d_x_t[j][1]+d_x_t[j][2])
                l_max1[0]=l_max1[0]+l1[0]
                l_max1[1]=l_max1[1]+l1[1]
                l_max1[2]=l_max1[2]+l1[2]
    x=df_test.iloc[i][5].split(' ')
    for j in x:
        if j in d_x_s.keys():
            if((d_x_s[j][0]+d_x_s[j][1]+d_x_s[j][2])!=0):
                l2[0]=d_x_s[j][0]/(d_x_s[j][0]+d_x_s[j][1]+d_x_s[j][2])
                l2[1]=d_x_s[j][1]/(d_x_s[j][0]+d_x_s[j][1]+d_x_s[j][2])
                l2[2]=d_x_s[j][2]/(d_x_s[j][0]+d_x_s[j][1]+d_x_s[j][2])
                l_max2[0]=l_max2[0]+l2[0]
                l_max2[1]=l_max2[1]+l2[1]
                l_max2[2]=l_max2[2]+l2[2]
    p_max1[0]=(l_max[0]*0.81+l_max1[0]*0.19)*0.996+(l_max2[0]*0.004)
    p_max1[1]=(l_max[1]*0.81+l_max1[1]*0.19)*0.996+(l_max2[1]*0.004)
    p_max1[2]=(l_max[2]*0.81+l_max1[2]*0.19)*0.996+(l_max2[2]*0.004)
    output.append(p_max1.index(max(p_max1)))
f=open("result2.txt",'w+')
out_str=""
f.writelines("record_id\ttopic_id\n")
for i in range(len(output)):
    num=5001+i
    out_str=str(num)+'\t'+str(output[i])+'\n'
    f.writelines(out_str)
#f.writelines(["%s\n" % item  for item in output])
f.close()
