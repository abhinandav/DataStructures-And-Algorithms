def insertion(a):
    for i in range(1,len(a)):
        k=a[i]
        j=i-1
        while j>=0 and k<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=k
    return a
print(insertion([2,5,7,1,4,9,6]))

