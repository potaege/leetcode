from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        r = 0
        l = len(height) - 1
        max_list = 0

        while(r != l):

            min_height = height[r]
            if(height[l] < min_height):
                min_height = height[l]

            s = l - r
            quantity = min_height * s
            if(quantity > max_list):
                max_list = quantity

            if(height[l] > height[r]):
                r += 1
            else :
                l -= 1     


    
        return max_list

s =Solution()
print(s.maxArea([3,6,1]))



