class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let m = new Map()
        for (let i = 0; i < nums.length; i++){
            if (m.has(nums[i])){
                m.set(nums[i], m.get(nums[i])+1)
            }else {
                m.set(nums[i], 1)
            }
        }
        let arr = [...m].sort((a, b) => b[1]-a[1])
        console.log(arr)
        let r = []
        for (let i = 0; i < k; i++){
            r.push(arr[i][0])
        }
        return r;
    }
}
