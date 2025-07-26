from typing import List

class Solution:
    def partitionString(self, s: str) -> List[str]:

        list_s = list(s)
        output = {}
        str_i = ""

        for i in list_s:

            str_add = str_i + i 

            if(str_add in output):
                str_i += i
            else:
                output[str_add] =  0
                str_i = ""

        return list(output.keys())
        
        
        

s = Solution()
print(s.partitionString("abbccccd"))    
