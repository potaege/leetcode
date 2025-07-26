from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        len_nums = len(nums)
        i = 1
        n =nums[0]
        index = 1
        while(i < len_nums):
            
            if(n == nums[index]):
                nums.pop(index)
            else:
                n = nums[index]
                index += 1
            
            i += 1
                     
        return  len(nums)
    

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))