"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

 

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

# ---------------- Solution 0 -----------  56 ms
# 修修补补终于通过，思路没错，但是代码写的太冗余，分支太多，有时间理清了再重写 2018.8.12
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 == 0:
            quotient, remainder  = divmod(l2, 2)
            return nums2[quotient] if remainder else (nums2[quotient-1] + nums2[quotient]) / 2.0

        if l2 == 0:
            quotient, remainder  = divmod(l1, 2)
            return nums1[quotient] if remainder else (nums1[quotient-1] + nums1[quotient]) / 2.0

        quotient, remainder  = divmod(l1 + l2, 2)
        l1_pass = 0
        l2_pass = 0
        will_pass = quotient + remainder - 1
        while l1_pass + l2_pass < will_pass:
            if l1_pass == l1:
                l2_pass += 1
            elif l2_pass == l2 or nums1[l1_pass] <= nums2[l2_pass] and l1_pass < l1:
                l1_pass += 1
            else:
                l2_pass += 1

        if remainder:
            if l2_pass == l2:
                return nums1[l1_pass]
            if l1_pass == l1:
                return nums2[l2_pass]
            return min(nums1[l1_pass], nums2[l2_pass])
        else:
            if l2_pass == l2:
                return (nums1[l1_pass] + nums1[l1_pass+1]) / 2.0
            if l1_pass == l1:
                return (nums2[l2_pass] + nums2[l2_pass+1]) / 2.0
            min1 = 0
            tag1 = 1
            min2 = 0
            tag2 = 1
            if l1_pass + 1 == l1:
                min2 = nums2[l2_pass]
                tag2 = 0
            if l2_pass + 1 == l2:
                min1 = nums1[l1_pass]
                tag1 = 0
            if tag1:
                min1 = min(nums1[l1_pass], nums2[l2_pass+1])
            if tag2:
                min2 = min(nums2[l2_pass], nums1[l1_pass+1])

            return (min1 + min2) / 2.0