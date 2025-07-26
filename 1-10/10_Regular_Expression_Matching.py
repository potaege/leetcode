class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        output = False

        list_str_1 ,list_point_1  = self.formatStr(s)
        list_str_2 ,list_point_2  = self.formatStr(p)

        # t,c = list_str_1[::] ,list_point_1[::]

        # if(len(list_str_2) > len(list_str_1)):

        #     list_str_1 ,list_point_1 = list_str_2[::],list_point_2[::]
        #     list_str_2 ,list_point_2 = t,c
        
        i = 0
        j = 0
    
        while(1):
            if(((len(list_str_1)-i-1) == 0)  and (len(list_str_2)-j-1) == 0):
                if(list_str_1[i] == list_str_2[j]):
                    output = True
                    
                break
            ## เขียนดักกรณีตัวท้าย
            elif(list_str_1[i] == list_str_2[j] or (list_str_1[i] == "." or list_str_2[j] == ".")):
                

                if(list_point_1[i] == 0 and list_point_2[j] == 0 ):
                    i += 1
                    j += 1

                elif(list_point_1[i] == 1 and list_point_2[j] == 0):

                    print(f"i {i}")
                    print(f"j {j}")
                    x = list_str_2[j]
                    sw_str_1 = 0

                    for n in range(i+1,len(list_str_1)): ##  j ++

                        if(list_str_1[n] == x): # i++ j++
                            sw_str_1 = 1
                            break

                        if(n == len(list_str_1)-1):  #j++
                            sw_str_1 = 0
                        

                    if(sw_str_1):
                        i += 1
                        j += 1
                    else:
                        j +=1
                    print(f"i last {i}")
                    print(f"j last {j}")
                
                else:
                    return "owo"



            
           

        return output

    def formatStr(self , s):

        list_str = []
        point_str = []

        i = 0
        while(i < len(s)):
            
            if(i != len(s)-1 and s[i+1] == "*"):
                list_str.append(s[i])
                point_str.append(1)
                i += 1
            
            else:
                list_str.append(s[i])
                point_str.append(0)
            
            i += 1
            

        return list_str,point_str




s = Solution()
print(s.isMatch(".*","ab"))

#c*c*c*c
# a*c


#aaaaaaaab*n*w*
#a*aaaaaaaa

#baa
#a*a

#a*a
#a