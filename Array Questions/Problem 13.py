"""Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition."""

def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    ## NOTE: Elegant way to do swapping
    i = 0
    j = len(A) - 1
    while i < j: ## j will iterate down and i will iterate up.
        if A[i] % 2 == 1 and A[j] % 2 == 0:
            A[i], A[j] = A[j], A[i]
        if A[i] % 2 == 0:
            i = i + 1
        if A[j] % 2 == 1:
            j = j - 1
    return A
    
A = [3,1,2,4]

print(sortArrayByParity(A))
