class Solution:
    def convert(self, s: str, numRows: int) -> str:

        output = "" 
        row_t = numRows - 1
        for i in range(0,numRows):
            j = i
            
            sw = 1
            while(j < len(s)):

                if(i == 0 or i == numRows-1):
                    output += s[j]
                    if(numRows >= 2):
                        j += numRows+ numRows - 2
                    else:
                        j += 1

                else:
                
                    if(sw):
                        sw = 0
                        output += s[j]
                        j +=  (numRows -1 - i) + row_t
                     
                        
                    else:
                        sw = 1
                        output += s[j]
                        j += i *2
                        
                    
            row_t -= 1

            
        return output
    


s = Solution()
print(s.convert("AB",1))
