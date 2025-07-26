from typing import List

## ไม่ผ่านติดกรณีstr ยาว
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:

        output = []
    
        for i in range(0,len(words)):

            test = words.copy()        
            test.pop(i)
            
            num_list = 0
            for j in range(0,len(test)):
                
                k = 1
                num = 0
                ##แก้ตรงนี้ต่อ
                while(j != len(test)-1 and k <= len(test[j]) and k <= len(test[j+1])):
                    
                    str = test[j][:k]
                    
                    if(test[j+1].startswith(str)):
                        
                        num += 1
                        k += 1
                    else:
                        break
                
                
                if(num > num_list):
                    num_list = num
            
            

            output.append(num_list)       
        
        return output
    



s = Solution()
print(s.longestCommonPrefix(["bdbb","aba","ae","dff","b","afcff","fbdc"]))