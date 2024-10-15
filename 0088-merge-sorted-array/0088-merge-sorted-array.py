class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n =int) -> None:
        
        last = m+n-1
        while m>0 and n>0:
            if nums1[m-1]> nums2[n-1]:
                nums1[last] = nums1[m-1]
                m-=1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last-=1
        while n>0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last-1
                    
                
        


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         for i in range (0, len(nums1)):
#             if nums1[i] == 0 and len(nums2)>0:
#                 nums1[i] = nums2.pop(0)
#                 print(nums1)
#         nums1.sort()
#         return nums1
     
#         nums1[m:] = nums2
#         nums1.sort()