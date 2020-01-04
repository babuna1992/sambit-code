"""
8. WAP to find the 2nd smallest num from a list.
   alist = [10,6,2,8,9,5,1]

alist = [10,6,2,8,9,5,1]
count=0


for k in alist:
    count=count+1
while count!=0:
    i=0
    while (count-1)>i:
        if alist[i]>alist[i+1]:
            a=alist[i]
            alist[i]=alist[i+1]
            alist[i+1]=a
        i=i+1
    count=count-1   
print "2nd smallest no in the list is:",alist[1]
print alist
"""
alist = [10,6,2,8,9,5,1]

for j in range(len(alist)-1):
    
    
    for i in range(len(alist)-1):
        if alist[i]>alist[i+1]:
            a=alist[i]
            alist[i]=alist[i+1]
            alist[i+1]=a
        
     
print "2nd smallest no in the list is:",alist[1]
print alist
