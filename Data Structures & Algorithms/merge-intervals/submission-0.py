class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        j = 1
        intervals.sort()
        res = [intervals[0]]

        while j < len(intervals):
            end = res[-1][1]

            if end >= intervals[j][0]:
                res[-1][1] = max(intervals[j][1], end)
                j += 1
            else:
                res.append(intervals[j])
                j += 1
        
        return res
                
               
        