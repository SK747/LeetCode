"""Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array."""

def replaceElements(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """

    check = arr[0]
    delel = 0
    greatest = arr[0]
    
    for j in range(len(arr)):
        ## find greatest
        if arr[j] > greatest:
            greatest = arr[j]

    for i in range(len(arr)):
        if arr[i] == greatest: ## then look again because we may have reached the greatest value (and need to look for a new one)
            greatest = 0
            for j in range(i+1, len(arr)):
                ## find greatest
                if arr[j] > greatest:
                    greatest = arr[j]
        arr[i] = greatest
    arr.pop()
    arr.append(-1)
    return arr

arr = [17,18,5,4,6,1]

replaceElements(arr)

print(arr)