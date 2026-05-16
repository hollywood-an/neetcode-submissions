class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = []
        for s in stones:
            heapq.heappush(hq, -s)
        while len(hq) > 1:
            one = heapq.heappop(hq)
            two = heapq.heappop(hq)
            if (one != two):
                heapq.heappush(hq, one - two)
            else:
                heapq.heappush(hq, 0)
        return -heapq.heappop(hq)
        
