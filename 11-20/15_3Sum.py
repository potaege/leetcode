from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = {}

        map_nums = {}

        for i in nums:
            if(not(i in map_nums)):
                map_nums[i] = 0
            map_nums[i] += 1
        print(map_nums)
        
        for i in range(0,len(nums)):

            x = nums[i]
            for j in range(i+1,len(nums)):
                
                y = nums[j]
                z = (x+y)*-1
                
                list_xyz = [x,y,z]
                list_xyz.sort()

                if(z in map_nums and ((list_xyz[0],list_xyz[1],list_xyz[2]) not in output)):

                    if(((x == y or x == z) and (map_nums[x] < 2)) or (y == z and map_nums[y] < 2)):
                       continue
                    elif(x == y and x == z and map_nums[x] < 3):
                        continue
                    
                    output[list_xyz[0],list_xyz[1],list_xyz[2]] = 1
        
        ls = []
        keys = list(output.keys())
        for i in keys:
            ls.append(list(i))

        return ls
    

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))