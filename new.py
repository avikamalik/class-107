import csv
f=open("abc.csv")
file=csv.reader(f)
data=list(file)
data.pop(0)
weight=[]
for i in range(0,len(data)):
    num=data[i][2]
    weight.append(float(num))
sum=0
for i in weight:
    sum=sum+i
mean=sum/len(weight)
print (mean)

import statistics
mean=statistics.mean(weight)
print (mean)