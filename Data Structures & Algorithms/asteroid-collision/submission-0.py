class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        r = [asteroids.pop()]
        while len(asteroids) > 0:
            test = asteroids.pop()
            temp = r[-1]
            if (test < 0 and temp < 0 or test > 0 and temp > 0):
                r.append(test)
                continue
            # explode
            if abs(test) > abs(temp):
                r.pop()
                r.append(test)
            elif abs(test) == abs(temp):
                r.pop()
        r.reverse()
        return r