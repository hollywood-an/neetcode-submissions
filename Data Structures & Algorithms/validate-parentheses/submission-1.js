class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let arr =[]
        for (let i = 0; i < s.length; i++){
            if (s[i] == '(' || s[i] == '{' || s[i] == '['){
                arr.push(s[i])
            } else {
                if (s[i] == ')'){
                    if (arr.pop() != '(') return false;
                }
                if (s[i] == '}'){
                    if (arr.pop() != '{') return false;
                }
                if (s[i] == ']'){
                    if (arr.pop() != '[') return false;
                }
            }
        }
        if (arr.length != 0) return false;
        return true;
    }
}
