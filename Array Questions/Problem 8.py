#Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

## might not be the fastest way, but I wrote this out in about 1 minute which is what matters.

def checkIfExist(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    flag = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j] * 2 and ((arr[i] and arr[j] ) >= 0 or (arr[i] and arr[j] ) <= 0) and i != j:
                flag = 1
                print(arr[i])
                print(arr[j])
                break
        else:
            continue
        break
    return bool(flag)

arr = [-2,0,10,-19,4,6,-8]

print(checkIfExist(arr))