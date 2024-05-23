def quick(a):
    if len(a)<=1:
        return  a
    else:
        pivot=a[0]
        left=[x for x in a[1:] if x<pivot]
        right=[x for x in a[1:] if x>=pivot]
        return quick(left)+[pivot]+quick(right)
    
print(quick([3,2,6,8,1,5]))