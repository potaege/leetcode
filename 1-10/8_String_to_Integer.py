class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        output = ""
        min, max = -2**31, 2**31 - 1

        list_block = ['!', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', 
                      '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '|', '}', '~', '`','"']
        sw = 0
        sign_str = ""
        for i in range(0,len(s)):

            if(sw == 0 and i != len(s)-1 and (s[i] == "-" or s[i] == "+" ) and s[i+1].isdigit()):
                if(s[i] == "-"):
                    sign_str = s[i]
  
            elif (s[i].isdigit() and s[i] != 0):
                sw = 1
                output += s[i]
            
            elif(sw or s[i].isalpha() or s[i] in list_block):
                break

        if(output):
            output = sign_str + str(int(output))
        else :
            output = "0"
        
        output = int(output)

        if(output < min):
            output = min
        elif(output > max):
            output = max
            
        return output
    


s = Solution()
print(s.myAtoi("+1"))