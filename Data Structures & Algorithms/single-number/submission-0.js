class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    singleNumber(nums) {
        let m = new Map();
        for (let n of nums){
            if (m.has(n)){
                m.set(n, m.get(n)+1);
            }else {
                m.set(n, 1);
            }
        }
        console.log(m)
        for (const [key, value] of m){
            if (value ==1) return key;
        }
        return 0;
    }
}
