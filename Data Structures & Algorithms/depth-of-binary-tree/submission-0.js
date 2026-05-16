/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxDepth(root) {

        if (root === null){
            return 0;
        }
        let right = 1 + this.maxDepth(root.right);
        let left = 1 + this.maxDepth(root.left);
        if (right > left){
            return right;
        } else {
            return left;
        }
        
    }
}
