from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = {}

        map_nums = {}
        ls = []

        for i in nums:
            if(not(i in map_nums)):
                map_nums[i] = 0
                ls.append(i)
            map_nums[i] += 1
        
        i = 0
        for key in map_nums:
            
            x = key

            if(key == 0 and map_nums[0] >= 3):
                output[0,0,0] =  1
            
            for j in range(i+1,len(ls)):

                y = ls[j]
                z = (x+y)*-1
                
                list_xyz =  [x,y,z]
                list_xyz.sort()
                
                if(z in map_nums and (list_xyz[0],list_xyz[1],list_xyz[2]) not in output):

                    if((x == z and map_nums[x] < 2) or (y == z and map_nums[y] < 2)):
                        continue

                    output[list_xyz[0],list_xyz[1],list_xyz[2]] = 1
                
            i += 1  

        list_output = []
        for key in output:
            list_output.append(list(key))
                  
        return list_output
    

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))