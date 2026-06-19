class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minC = 0

        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        minC1 = cost[0]
        first, second = 1, 2
        while first < len(cost) and second < len(cost):
            if cost[first] < cost[second]:
                minC1 += cost[first]
                i = first
            else:
                minC1 += cost[second]
                i = second
            first = i + 1
            second = i + 2

        minC2 = cost[1]
        first, second = 2, 3
        while first < len(cost) and second < len(cost):
            if cost[first] < cost[second]:
                minC2 += cost[first]
                i = first
            else:
                minC2 += cost[second]
                i = second
            first = i + 1
            second = i + 2
        
        return min(minC1, minC2)  

        