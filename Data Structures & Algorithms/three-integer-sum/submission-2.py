class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r =  []
        nums.sort()
        if len(nums) < 4:
            return [] if nums[0] + nums[1] + nums[2] != 0 else [nums]
        already = set()
        for i in range(len(nums) - 2):
            if nums[i] in already:
                continue
            already.add(nums[i])
            target = 0 - nums[i]
            l = self.twoSum(nums[i+1:], target)
            print(l)
            for x in l:
                x.append(nums[i])
                if x not in r:
                    r.append(x)
        return r


    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        one = 0
        two = len(numbers) - 1
        r = []
        while one < two:
            if numbers[one] + numbers[two] == target:
                r.append([numbers[one], numbers[two]])
                one = one + 1
            elif numbers[one] + numbers[two] > target:
                two = two - 1
            else:
                one = one + 1
        return r