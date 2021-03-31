#Given an array of integers arr, return true if and only if it is a valid mountain array.

## Kind of dirty solution but 71% better 

def validMountainArray(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    flag = 0
    upflag = 0
    downflag = 0
    for i in range(len(arr)-1):
        if arr[i+1] == arr[i]:
            upflag = 0
            break
        elif arr[i+1] > arr[i]:
            if downflag == 1:
                upflag = 0
                break
            else:
                upflag = 1
        elif arr[i+1] < arr[i]:
            if upflag != 1:
                break
            else:
                downflag = 1
    if downflag == 1 and upflag == 1:
        flag = 1
    return bool(flag)

arr = [14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]
print(validMountainArray(arr))