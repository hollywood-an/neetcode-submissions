class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let saved = [...nums]
        console.log(saved)
        let s = nums[Math.floor(nums.length/2)]
        console.log(s)
        while (s != target && nums.length > 1){
            if (s < target){
                nums = nums.splice(nums.length/2 + 1, nums.length)
            } else {
                nums = nums.splice(0, nums.length/2)
            }
            console.log(nums)
            s = nums[Math.floor(nums.length/2)]
            console.log(s)
        }
        
        if (s == target) return saved.indexOf(s);
        return -1;
    }
}
