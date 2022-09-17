class Solution(object):
    def insert(self, intervals, newInterval):
        arr = []
        high = 0
        for i in range(len(intervals)):
            if intervals[i[1]] < newInterval[0]:
                arr.append(intervals[i])
            
            elif intervals[i[0]] > newInterval[1]:
                arr.append(intervals[i])
            
            elif intervals[i[0]] < newInterval[0] and intervals[i[1]] < newInterval[1]:
                newmin = intervals[i[0]]
            
            elif intervals[i[0]] < newInterval[0] and intervals[i[1]] < newInterval[1]:
                newmin = intervals[i[0]]
            
        return arr



intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
s = Solution()
print(s.insert(intervals, newInterval))