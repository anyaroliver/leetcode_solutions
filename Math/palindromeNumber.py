# Problem number: 9 on LeetCode
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            if x // div != x % 10: return False
            x = (x % div) // 10
            div = div / 100
        return True

# Create an object
sol = Solution()

# Test the function
print(sol.isPalindrome(121))    # True
print(sol.isPalindrome(-121))   # False
print(sol.isPalindrome(123))    # False
print(sol.isPalindrome(1221))   # True