class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let first = 0; 
        let second = nums.length;
        while (first < second){
            let middle = first + Math.floor((second - first)/2)
            if (nums[middle] == target){
                return middle
            } 
            if (nums[middle] > target){
                second = middle ;
            } else {
                first = middle + 1;
            }
        }
        return -1;
    }
}
