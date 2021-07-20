def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    print(s[1:])
    if len(s) == 0:
        return s
    else:
        return reverseString(s[1:]) + s[0] ## (basically only s[0] is being returned)
        
x = reverseString('John')
print(x)