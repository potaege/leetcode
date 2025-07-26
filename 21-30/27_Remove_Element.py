from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        len_nums = len(nums)
        index = 0
        
        for i in range(0,len_nums):

            if(nums[index] == val):
                nums.pop(index)
            else :
                index += 1
            i += 1

    
        return len(nums)
        

s = Solution()
print(s.removeElement([3,2,2,3],3))