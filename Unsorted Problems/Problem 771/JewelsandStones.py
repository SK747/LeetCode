class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for c in range(len(stones)):
            for d in range(len(jewels)):
                if jewels[d] == stones[c]:
                    count += 1
        return count

s = Solution()
jewels = 'aA'
stones = 'aaabbA'
print(s.numJewelsInStones(jewels, stones))