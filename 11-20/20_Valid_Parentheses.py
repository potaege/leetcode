class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
    
        output = True
        for i in s:
           
            if(i == "(" or i == "{" or i == "["):
                sw = 1
                stack.insert(0, i)
            
            elif(i == ")" and len(stack) > 0 and stack[0] == "("):
                stack.pop(0)
            elif(i == "}" and len(stack) > 0 and  stack[0] == "{"):
                stack.pop(0)
            elif(i == "]" and len(stack) > 0 and  stack[0] == "["):
                stack.pop(0)

            else:
                output =False
                break
        
        if(stack != []):
            output = False
                
        return output
    

s = Solution()
print(s.isValid("()[]{}"))