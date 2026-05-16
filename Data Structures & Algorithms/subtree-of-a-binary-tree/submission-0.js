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
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    isSubtree(root, subRoot) {

        if (this.isSameTree(root, subRoot)){
            return true;
        }

        if (root == null){
            return false;
        }

        let left = this.isSubtree(root.left, subRoot);
        let right = this.isSubtree(root.right, subRoot);

        return left || right;

        
    }

    isSameTree(p, q) {

        if (p == null && q == null) return true;

        if (p == null || q == null) return false;

        if (p.val != q.val) return false;

        let right = this.isSameTree(p.right, q.right);
        let left = this.isSameTree(p.left, q.left);

        return right && left;

    }
}
