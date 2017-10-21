def mySum(a):
    s=0
    aa=open(a)
    for i in aa:
        #print(i)
        j = i.split()
        #print(j)
        for g in range(0,len(j),1):
            #print(g)
            s=s+int(j[g])
    return s

f=mySum("G:/python/t.txt")
print("total sum is :",f)
