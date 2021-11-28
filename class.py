import csv
import statistics
import math
f=open("class2.csv")
file=csv.reader(f)
data=list(file)
data.pop(0)
marks=[]
for i in range(0,len(data)):
    num=data[i][1]
    marks.append(float(num))

sum=0
for i in marks:
    sum=sum+i
mean=sum/len(marks)
print (mean)


square=[]
for i in marks:
    a=int(i)-mean
    a=a*a
    square.append(a)
sum=0
for i in square:
    sum=sum+i
result=sum/(len(marks)-1)
d=math.sqrt(result)
print (d)


d=statistics.stdev(marks)

print (d)


