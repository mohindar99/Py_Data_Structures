
def merge(custlist,l,m,r):
    n1=m-l+1
    n2=r-m
    L=[0]*(n1)
    R=[0]*(n2)

    for i in range(n1):
        L[i]=custlist[l+i]
    for j in range(n2):
        R[j]=custlist[m+j+1]

    i,j,k=0,0,l

    while i<n1 and j<n2:
        if L[i]<=R[j]:
            custlist[k]=L[i]
            i+=1
        else:
            custlist[k]=R[j]
            j+=1
        k+=1

    while i<n1:
        custlist[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        custlist[k]=R[j]
        j+=1
        k+=1

def merge_sort(custlist,l,r):
    if l>=r:
        return
    m=(l+(r-1))//2
    merge_sort(custlist,l,m)
    merge_sort(custlist,m+1,r)
    merge(custlist,l,m,r)
    return custlist

print(merge_sort([1,3,2,5,4,6,7,8,9,10],0,9))