#二分查找

#线性查找
def LinearSearch(array,t):
    for i in range(len(array)):
        if array[i] == t:
            return True
        return False
#二分查找
def BinarySearch(array,t):
    left = 0
    right = len(array) - 1
    while left < right:
        mid = int((left + right) / 2)
        if array[mid] < t:
            left = mid + 1
        elif array[mid] > t:
            left = mid -1
        else:
            return True
    return False

#二分查找的变种(矩阵查找)
#matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
class Solution:
    def searchMatrix(self,matrix,target):
        i = 0
        j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] == target:
                j -= 1
            else:
                i += 1
        return False