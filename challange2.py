__author__ = 'sunkumar'
import scipy
import numpy as np;
import pandas as pd;
import math;
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
#d_x_s={}
for i in range(0,len(df_train[3])):
    x=df_train.iloc[i][3].split(';')
    for j in x:
        if j in d_x_a.keys():
            d_x_a[j][df_train.iloc[i][2]-2043]=d_x_a[j][df_train.iloc[i][2]-2043]+1
        else:
            d_x_a[j]=[0,0,0,0,0,0,0,0,0,0,0,0]
            d_x_a[j][df_train.iloc[i][2]-2043]=d_x_a[j][df_train.iloc[i][2]-2043]+1
    #x=df_train.iloc[i][4].split(' ')
    #for j in x:
    #    if j in d_x_t.keys():
    #        d_x_t[j][df_train.iloc[i][2]-2043]=d_x_t[j][df_train.iloc[i][2]-2043]+1
    #    else:
    #        d_x_t[j]=[0,0,0,0,0,0,0,0,0,0,0,0]
    #        d_x_t[j][df_train.iloc[i][2]-2043]=d_x_t[j][df_train.iloc[i][2]-2043]+1
#print(d_x_a)
suc_count=0
fail_count=0
error=0
total_error=0
val_a_a=[]

for i in range(0,len(df_test[3])):
    l=[0,0,0,0,0,0,0,0,0,0,0,0]
    l_max=[0,0,0,0,0,0,0,0,0,0,0,0]
    l1=[0,0,0,0,0,0,0,0,0,0,0,0]
    l_max1=[0,0,0,0,0,0,0,0,0,0,0,0]
    l2=[0,0,0,0,0,0,0,0,0,0,0,0]
    l_max2=[0,0,0,0,0,0,0,0,0,0,0,0]
    #p_max=[-1,-1,-1]
    p_max1=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    x=df_test.iloc[i][3].split(';')
    val_a=0
    for j in x:
        if j in d_x_a.keys():
            sum_prob=0
            if(sum(d_x_a[j])!=0):
                for k in range(0,12):
                    sum_prob=sum_prob+(k*d_x_a[j][k])
                for k in range(0,12):
                    if(sum_prob!=0):
                        l[k]=(k*d_x_a[j][k])/sum_prob
                        l_max[k]=l_max[k]+l[k]
                        if(l_max[k]>0.5):
                            val_a=k-1
                            break
    if((df_test.iloc[i][1]==0) or (df_test.iloc[i][1]==0)):
        val_a=((val_a*0)+(6*2))/2
    else:
        val_a=((val_a*1)+(6*1))/2
    if((val_a*2)%2!=0):
        val_a=val_a-0.5
    val_a=int(val_a+2043)
    val_a_a.append(val_a)
    #p_max=max(l_max[0],l_max[1],l_max[2])
    #x=df_test.iloc[i][5].split(' ')
    #for j in x:
    #    if j in d_x_t.keys():
    #        if(sum(d_x_t[j])!=0):
    #            for k in range(0,12):
    #                l1[k]=d_x_t[j][k]/sum(d_x_t[j])
    #                l_max1[k]=l_max1[k]+l1[k]
    #for i in range(0,12):
    #    p_max1[i]=l_max[i]*1.0+l_max1[i]*0
    #print(p_max1.index(max(p_max1))+2043)

f=open("result13.txt",'w+')
out_str=""
f.writelines("record_id\tpublication year\n")
for i in range(0,len(val_a_a)):
    num=5001+i
    out_str=str(num)+'\t'+str(val_a_a[i])+'\n'
    f.writelines(out_str)
#f.writelines(["%s\n" % item  for item in output])
f.close()

#print(d_x_a)
#df1 = pd.read_csv("C:/Users/sunkumar/Desktop/output/output.txt",header=None,sep='\t')
#df1
