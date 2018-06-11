#插入排序
#python实现
def insertSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A
A = [5,2,4,6,1,3]
print(insertSort(A))

#js实现
function insertSort(A){
    for (j = 1;j < A.length; j++){
        var key = A[j];
        var i = j - 1;
        while (i >= 0 && A[i] >key){
            A[i + 1] = A[i];
            i = i - 1;
        }
        A[i + 1] = key;
    }
    return A;
}
var A = [5,2,4,6,1,3];
console.log(insertSort(A));