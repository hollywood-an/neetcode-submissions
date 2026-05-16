class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                continue
            p *= nums[i]
        r = []
        print(p)
        if zeros > 1:
            return [0] * len(nums)
        if zeros == 1:
            r = [0] * len(nums)
            for j in range(len(nums)):
                if nums[j] == 0:
                    r[j] = p
                    return r
        for j in range(len(nums)):
            r.append(int(p/nums[j]))
        return r