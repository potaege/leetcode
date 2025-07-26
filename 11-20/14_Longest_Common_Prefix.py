from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        str_match = strs[0]

        if(len(strs) >= 2):
            
            i = 0

            while(i <len(strs[0]) and i<len(strs[1])):
                if(strs[0][i] != strs[1][i]):
                    break
                i += 1

            str_match = strs[0][:i]
            
            for j in range(2,len(strs)):
                
                if(str_match != strs[j][:i]):
                    
                    while(str_match != strs[j][:i] and i > 0):
                        i -= 1
                        str_match = str_match[:i]
                    

                j += 1

        return str_match
    



s = Solution()
print(s.longestCommonPrefix([""]))