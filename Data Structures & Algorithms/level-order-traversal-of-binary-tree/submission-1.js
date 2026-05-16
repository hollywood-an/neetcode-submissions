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
     * @return {number[][]}
     */
    levelOrder(root) {
        if (root == null) return [];
        let queue = [root];
        let r = [];
        while (queue.length != 0){
            let arr = [];
            let level = queue.length;
            for (let i = 0; i < level; i++){
                let first = queue.shift();
                arr.push(first.val);
                if (first.left) {queue.push(first.left);}
                if (first.right) {queue.push(first.right);}
            }
            r.push(arr);
        }
        return r;
    }
}
