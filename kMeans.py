import pandas as pd
import math as mt

data=pd.read_csv("data1.csv",header=None,dtype=float)

col1=[]
col2=[]

for i in data[0]:
    col1.append(i)
    
for i in data[1]:
    col2.append(i)
    
k = int(input("Enter value of k : "))

m=pd.DataFrame()
rows = data.loc[0:k-1,:]
m=m.append(rows)

print(m)

mean=[]
clusterPrev=[]
cluster=[]

while True:    
    for i in range(len(data)):
        for j in range(len(m)):
            mean.append(mt.sqrt((data[0][i]-m[0][j])**2+(data[1][i]-m[1][j])**2))
        min=0
        for j in range(1,len(m)):
            if mean[j]<mean[min]:
                min=j
        cluster.append(min+1)
    
        mean.clear()
        
    if cluster == clusterPrev:
        break;
    else:
        clusterPrev=cluster[:]
        
        m=m.replace(m,0)
            
        for i in range(len(cluster)):
            m[0][cluster[i]-1] += data[0][i]
            m[1][cluster[i]-1] += data[1][i]
        
        for i in range(k):
            m[0][i] /= cluster.count(i+1)
            m[1][i] /= cluster.count(i+1)
        cluster.clear()
    
    
print(cluster)
print(clusterPrev)
