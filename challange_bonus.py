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
df_train = df
#df_test = df[df[0]>2500]

# auth=[]
# topi=[]
# summ=[]
# word=[]
#print(df_train)
x=[]
d_x_a={}
d_x_t={}
d_x_s={}
for i in range(0,len(df_train[3])):
    count1=0
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
#suc_count=0
#fail_count=0
for p in range(0,3):
    count=0
    d_x_a_o=[]
    d_x_t_o=[]
    d_x_s_o=[]
    for i,j in d_x_a.items():
        if((j[(p+1)%3]==0) and (j[(p+2)%3]==0) and (j[p]>1)):
            #print(d_x_a[i])
            d_x_a_o.append(i)
            count=count+1
            if(count>10):
                break
    count=0
    for i,j in d_x_t.items():
        if((j[(p+1)%3]==0) and (j[(p+2)%3]==0) and (j[p]>1)):
            #print(d_x_t[i])
            d_x_t_o.append(i)
            count=count+1
            if(count>50):
                break
    count=0
    for i,j in d_x_s.items():
        if((j[p]>j[(p+1)%3]) and (j[p]>j[(p+2)%3])):
            d_x_s_o.append(i)
            count=count+1
            if(count>200):
                break
    f=open("result20.txt",'a')
    out_str=""
#f.writelines("record_id\tpublication year\n")
    for i in range(0,10):
        str1=' '.join(d_x_t_o[(6*i):(6*i)+6])
        str2=' '.join(d_x_s_o[15*i:(15*i)+15])
        num=count1
        out_str=str(num)+'\t'+str(p)+'\t'+'2049\t'+d_x_a_o[i]+'\t'+str1+'\t'+str2+'\n'
        f.writelines(out_str)
        count1=count1+1
#f.writelines(["%s\n" % item  for item in output])
    f.close()

