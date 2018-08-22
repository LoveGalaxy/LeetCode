"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # ---------------- Solution 0 -----------
        r_list = []
        for i in range(rowIndex+1):
            t = r_list[:]
            for j in range(i+1):
                if j == i:
                    r_list.append(1)
                elif j == 0:
                    pass
                else:
                    r_list[j] = t[j-1] + t[j]
        return r_list