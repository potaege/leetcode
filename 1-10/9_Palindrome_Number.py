class Solution:
    def isPalindrome(self, x: int) -> bool:

        s = str(x)
        re_s = s[::-1]

        return s == re_s
    

s = Solution()
print(s.isPalindrome(123))