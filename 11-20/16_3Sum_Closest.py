from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        map_nums = {}
        ls = []

        for i in nums:
            if(i not in map_nums):
                map_nums[i] = 0
                ls.append(i)
            map_nums[i] += 1
        
        
        return 1
    



nums = []
target = []

s = Solution()
print(s.threeSumClosest(nums,target))
