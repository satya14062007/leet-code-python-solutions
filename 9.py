class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (except 0) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0

        # Reverse only half of the digits
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        # Even digits: x == rev
        # Odd digits: x == rev // 10
        return x == rev or x == rev // 10
