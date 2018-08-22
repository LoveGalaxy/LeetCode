"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # ---------------- Solution 0 -----------
        r_list = []
        for i in range(numRows):
            list = []
            for j in range(i+1):
                if j == 0 or j == i:
                    list.append(1)
                else:
                    list.append(r_list[i-1][j-1] + r_list[i-1][j])
            r_list.append(list)
        return r_list