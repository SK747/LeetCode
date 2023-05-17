from collections import defaultdict

def ValidSudoku(nums):

    hashset1 = set()
    hashdict1 = defaultdict(set)
    hashdict2 = defaultdict(set)

    for j in range(len(nums)):
        for i in range(len(nums[j])):
            if nums[j][i] == '.':
                continue
            elif nums[j][i] not in hashset1 and nums[j][i] not in hashdict1[i] and nums[j][i] not in hashdict2[(j//3,i//3)]:
                hashset1.add(nums[j][i])
                hashdict1[i].add(nums[j][i])
                hashdict2[(j//3,i//3)].add(nums[j][i])
                #print('I and J are', i,'and', j, 'Nums is', nums[j][i],',', hashset1)
                #print(hashdict2)
                #print(hashdict1)
            else:
                return True
        hashset1.clear()
    return False

print(ValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
