#extract data from web assignment 1
import re
data=open('regex_sum_1510920.txt')
numlist=list()
for line in data:
    line=line.rstrip()
    stuff=re.findall('[0-9]+',line)
    num0=[float(x) for x in stuff]
    num=sum(num0)
    numlist.append(num)
print('Sum:' , sum(numlist))
