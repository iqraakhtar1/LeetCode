class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        list1 = []
        list2 = []
        
        for i in nums1:
            if i not in nums2:
                list1.append(i)
        for j in nums2:
            if j not in nums1:
                list2.append(j)
        return(list1, list2)
            
        