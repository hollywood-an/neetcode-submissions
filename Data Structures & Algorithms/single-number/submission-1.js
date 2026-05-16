class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    singleNumber(nums) {
        if (nums.length == 1) return nums[0];
        let z = 0;
        for (let i = 0; i < nums.length; i++){
            z = z ^ nums[i];
        }
        return z
    }
}
