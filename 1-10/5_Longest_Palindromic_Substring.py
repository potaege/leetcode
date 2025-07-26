class Solution(object):
    def longestPalindrome(self, s):
        
        i = 0
        right_str = len(s) 
        output = ""

        while(right_str):

            for i in range(0,right_str):
                str = s[i:right_str]

                if(str == str[::-1] and len(str) > len(output)):
                    output = str

            right_str -= 1

        return output


s = Solution()
print(s.longestPalindrome("a"))