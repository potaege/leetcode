class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        ls  = []
        
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)

        while(len_nums1 or len_nums2):
            
            if(len_nums1 and len_nums2):
                
                if(nums1[len(nums1) - len_nums1] >= nums2[len(nums2) - len_nums2] ):
 
                    ls.append(nums2[len(nums2) - len_nums2])
                    len_nums2 -= 1
                elif(nums1[len(nums1) - len_nums1] < nums2[len(nums2) - len_nums2] ):
                    ls.append(nums1[len(nums1) - len_nums1])
                    len_nums1 -= 1
                         
            elif(len_nums1):
                ls.append(nums1[len(nums1) - len_nums1])
                len_nums1 -= 1
            elif(len_nums2):
                ls.append(nums2[len(nums2) - len_nums2])
                len_nums2 -= 1

        len_all = len(nums1) + len(nums2)

        if(len_all%2):
            index = int(len_all/2) 
            output = float(ls[index]) /1
        else :
            index = int(len_all/2)
            output = (float(ls[index]) + float(ls[index-1])) /2

        return output
    

s = Solution()
print(s.findMedianSortedArrays([1,3],[2]))