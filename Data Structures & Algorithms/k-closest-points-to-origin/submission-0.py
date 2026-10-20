from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_distance = []

        for point in points:
            x1 = point[0]
            y1 = point[1]

            distance = (sqrt((x1)**2 + (y1)**2))
            points_distance.append((distance, point))

        heapq.heapify(points_distance)
        res = []

        while k > 0:
            distance, point = heapq.heappop(points_distance)

            res.append(point)

            k -= 1
        
        return res

        