class Solution(object):
    def twoSum(self, nums, target):

        output = []
        i = 0
        while(i<len(nums)):

            total = target-nums[i]

            if(total == nums[i] and nums.count(total) >= 2):

                reversed_nums = nums[::-1]
                output = [i, len(nums) - reversed_nums.index(total) - 1]
                return output
            
            elif(nums.count(total) and total != nums[i]):

                output = [i, nums.index(total)]
                return output

            i += 1


s = Solution()
print(s.twoSum([2,5,5,11] ,10))