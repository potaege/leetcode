class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        output = -1
        index = 0

        len_needle = len(needle)
  
        while(index < len(haystack)):
           
            if(index+len_needle <= len(haystack) and haystack[index:index+len_needle] == needle):
                output = index
                break
            
            
            index += 1

        return output
    

s = Solution()
print(s.strStr("adbutsad","sad"))
print(len("adbutsad"))