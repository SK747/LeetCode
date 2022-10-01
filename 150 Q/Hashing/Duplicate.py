## Hashmap

## This is extremely simple
## A hashmap can be used to store whether we have seen a character or not
## Checking a hashmap is an O(1) operation, so we just iterate over the list once
## O(n) algorithm
## 2.5 minutes

def ContainsDuplicate(nums):
    hashset = set()
    for i in range(len(nums)):
        if nums[i] in hashset:
            return True
        else:
            hashset.add(nums[i])
    return False

print(ContainsDuplicate([1,2,3]))
