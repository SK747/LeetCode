from collections import defaultdict

hashset1 = set()
hashdict1 = defaultdict(set)
hashdict2 = defaultdict(set)
nums = [["1","2","4","7"],["5","6","2","4"],["3","2","5","9"]]

for j in range(len(nums)):
    for i in range(len(nums[j])):
        if nums[j][i] not in hashset1 and nums[j][i] not in hashdict1[i] and nums[j][i] not in hashdict2[[j//3,i//3]]:
            hashset1.add(nums[j][i])
            hashdict1[i].add(nums[j][i])
            print('I and J are', i,'and', j, 'Nums is', nums[j][i],',', hashset1)
        else:
            print('True')

    hashset1.clear()