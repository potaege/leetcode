class Solution:
    def reverse(self, x: int) -> int:
        
        output = ""
        min, max = -2**31, 2**31 - 1
        s = str(x)
        if(s[0] == "-"):
            s = s[1:]
            s = s[::-1]
            num = int(s)
            output = "-" + str(num)
        else:
            s = s[::-1]
            num = int(s)
            output =  str(num)
        
        output = int(output)
        if(output < min or output > max):
            output = 0
        return output
    

s = Solution()
print(s.reverse(1534236469))