import csv
import statistics
f=open("abc.csv")
file=csv.reader(f)
data=list(file)
data.pop(0)
weight=[]
for i in range(0,len(data)):
    num=data[i][2]
    weight.append(float(num))
height.sort()
n=len(height)
if n%2==0:
    m1=float(height[n//2])
    m2=float(height[n//2+1])
    median=(m1+m2)/2
else:
    median=float(height[n//2])
print (median)

median=statistics.median(height)
print (median)