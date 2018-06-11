#快速排序
def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i = i +1
            A[i],A[j] = A[j],A[i]
    A[i + 1],A[r] = A[r],A[i + 1]
    return i + 1

def quickSort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

A = [2,8,7,1,3,5,6,4]
quickSort(A,0,7)
print(A)

# 在数组元素数量为n的数组里面寻找第k大的数
def findKthLargest(A,p,r,k):
    if p <= r:
        q = partition(A,p,r)
        if k - 1 == q:
            return A[q]
        elif k - 1 < q:
            return findKthLargest(A,p,q-1,k)
        else:
            return findKthLargest(A,q+1,r,k)
A = [2,8,7,1,3,5,6,4]
ret = findKthLargest(A,0,7,8)
print(ret)
