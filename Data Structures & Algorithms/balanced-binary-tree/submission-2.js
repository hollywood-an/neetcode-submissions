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
     * @return {boolean}
     */
    isBalanced(root) {
        if (root == null) return true;

        function height(root){
            if (root == null) return 0;

            let left = 1 + height(root.left);
            let right = 1 + height(root.right);
            if (right > left){
                return right;
            } else {
                return left;
            }
        }

        return (Math.abs(height(root.right) - height(root.left)) <= 1) && this.isBalanced(root.right) && this.isBalanced(root.left);

    }
}
