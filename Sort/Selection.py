def selection(a):
    for i in range(len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]

a=[3,2,6,3,7,8,5]
selection(a)
print(a)
            

def selection2(a):
    i=0
    n=len(a)-1
    while i<n:
        min=i
        j=i+1
        while j<n:
            if a[j]<a[min]:
                min=j
            j+=1
        a[i],a[min]=a[min],a[i]
        i+=1
a=[3,2,6,3,7,8,5]
selection2(a)
print(a)
           