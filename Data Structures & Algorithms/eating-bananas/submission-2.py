class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        while left < right:
            mid = (left + right)//2
            hours = 0
            for p in piles:
                hours = hours + 1 + (p - 1)//mid
            print(hours)
            if hours == h:
                result = mid
                break
            elif hours > h:
                left = mid + 1
            else:
                right = mid - 1
                result =  mid

        return result
