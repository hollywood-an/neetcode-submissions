class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        for point in points:
            heapq.heappush(hq, (math.sqrt(point[0] ** 2 + point[1] ** 2), [point[0], point[1]]))
        r = []
        for i in range(k):
            r.append(heapq.heappop(hq)[1])
        return r
