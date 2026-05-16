class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        
        fleets = 0
        slowest = 0
        for p, s in cars:
            time = (target-p)/s
            if time > slowest:
                fleets += 1
                slowest = time

        return fleets
                