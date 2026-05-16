class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const cleaned = s.replace(/[^a-z0-9]/gi, "");
        const b = cleaned.toLowerCase();
        for (let i = 0; i < b.length/2; i++){
            if (b[i] != b[b.length - 1 - i]) return false;
        }
        return true;
    }
}
