class Solution:
    def romanToInt(self, s: str) -> int:

        list_roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        output = 0
        sw = 1

        total = list_roman[s[0]]

        for i in s[1:]:
        
            n = list_roman[i]

            if(sw) :
                if(total >= n):
                    output += total
                    total = n

                elif(n > total):
                    output += n - total
                    total = 0
                    sw = 0
            else:
                total += n
                sw = 1
      
        output += total     

        return output
    


s = Solution()
print(s.romanToInt("MCMXCIV"))