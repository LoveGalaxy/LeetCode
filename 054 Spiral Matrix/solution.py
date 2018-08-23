"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # ---------------- Solution 0 -----------         
        if matrix == [[]] or matrix == []:
            return []
        
        r_list = []
        h = len(matrix)
        w = len(matrix[0])
        s = [[0 for i in range(w)] for j in range(h)]
        
        def step(i, j, direction):
            if direction == 0: # east
                if j+1 >= w or s[i][j+1] == 1:
                    return i+1, j, 1
                else:
                    return i, j+1, 0
            elif direction == 1: # south
                if i+1 >= h or s[i+1][j] == 1:
                    return i, j-1, 2
                else:
                    return i+1, j, 1
            elif direction == 2: # west
                if j-1 < 0 or s[i][j-1] == 1:
                    return i-1, j, 3
                else:
                    return i, j-1, 2
            else: # north
                if i-1 < 0 or s[i-1][j] == 1:
                    return i, j+1, 0
                else:
                    return i-1, j, 3
        i = 0
        j = 0
        direction = 0
        while True:
            if i >= h or j >= w or s[i][j] == 1:
                break;
            s[i][j] = 1
            r_list.append(matrix[i][j])
            i, j, direction = step(i, j, direction)
        return r_list