import csv
import statistics
f=open("abc.csv")
file=csv.reader(f)
data=list(file)
data.pop(0)
height=[]
for i in range(0,len(data)):
    num=data[i][1]
    height.append(float(num))
mode=statistics.mode(height)
print(mode)