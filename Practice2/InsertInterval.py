class Solution(object):
    def insert(self, intervals, newInterval):
        arr = []
        for i in range(len(intervals)):
            arr.append(intervals[i])
        return arr



intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
s = Solution()
print(s.insert(intervals, newInterval))