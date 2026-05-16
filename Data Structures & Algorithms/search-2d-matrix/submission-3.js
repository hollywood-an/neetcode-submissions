class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        let l = 0;
        let g = matrix.length;
        let middle = l + Math.floor((g-l)/2)
        while (l < g){
            middle = l + Math.floor((g-l)/2)
            if (matrix[middle][0] == target)return true;
            if (target > matrix[middle][0] && target <= matrix[middle][matrix[0].length - 1]){
                break;
            } 
            if (target> matrix[middle][0]){
                l = middle + 1;
            } else {
                g = middle;
            }
        }
        console.log(middle)
        // correct row in middle now
        l = 0;
        g = matrix[0].length ;
        let middle2 = l + Math.floor((g-l)/2)
        while (l < g){
            middle2 = l + Math.floor((g-l)/2)
            let n = matrix[middle][middle2]
            if (n == target) return true;
            if (target > n){
                l = middle2 + 1;
            } else {
                g = middle2;
            }
        }
        return false;
    }
}
