class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        rev = 0

        while x != 0:
            digit = int(x % 10)

            # Handle negative numbers correctly
            if x < 0 and digit > 0:
                digit -= 10

            x = int((x - digit) / 10)

            # Overflow check
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0
            if rev < INT_MIN // 10 or (rev == INT_MIN // 10 and digit < -8):
                return 0

            rev = rev * 10 + digit

        return rev
