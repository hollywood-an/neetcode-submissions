class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = digits[len(digits)-1] + 1
        if digit < 10:
            digits.pop()
            digits.append(digit)
        else:
            digits[len(digits) - 1] = 0
            carry = True
            for i in range(len(digits)-2, -1, -1):
                print("run")
                digits[i] = digits[i] + 1
                if digits[i] < 10:
                    carry = False
                    break
                digits[i] = 0
            if carry:
                digits.insert(0, 1)
        return digits