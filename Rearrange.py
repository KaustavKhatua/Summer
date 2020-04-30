def arrange_function(a):
    index=len(a)-1
    i=0
    while i<index:
        if a[i]<0:
            while a[index]<0 and index>0:
                index=index-1
            if index<=i:
                break
            b=a[index]
            a[index]=a[i]
            a[i]=b
            index=index-1
        i=i+1
    return a
# a=[-2,-2,-2,1]
# a=[-6,7,10,-14,2,-12,8,9]
a=[-4,-4,-4,-4]
print(arrange_function(a))
