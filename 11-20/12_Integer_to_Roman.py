class Solution:
    def intToRoman(self, num: int) -> str:

        list_roman = {
            1 : "I",
            5 : "V",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M"
        }

        output = ""

        len_n = len(str(num))
        str_n = str(num)

        i = 0
        while(i < len_n):

            n = 10 ** (len_n-i-1)
            
            total= int(str_n[i])
            if(total <=3):
                output += list_roman[n] * total
            elif(total == 4 or total == 9):
                total += 1
                output += list_roman[n] + list_roman[total*n]
                
            else:
                total -= 5
                output += list_roman[5*n] + list_roman[n] * total

            i += 1  

        return output
    

s = Solution()
print(s.intToRoman(1459))