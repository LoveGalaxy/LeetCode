"""
On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid. 

Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 

Eventually, we reach all R * C spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.

 

Example 1:

Input: R = 1, C = 4, r0 = 0, c0 = 0
Output: [[0,0],[0,1],[0,2],[0,3]]


 

Example 2:

Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]



Note:

1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C
"""

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        # ---------------- Solution 0 ----------- 
        def is_over(A, R, C):
            for C in A:
                if 0 in C:
                    return False
            return True

        def in_grid(R, C, r0, c0):
            if 0 <= r0 < R and 0 <= c0 < C:
                return True
            else:
                return False

        def go_direction(direction, r, c):
            if direction == 0: # east
                c += 1
            elif direction == 1: # south
                r += 1
            elif direction == 2: # west
                c -= 1
            else: # north
                r -= 1
            return r, c

        r_list = []
        A = [[0 for i in range(C)] for i in range(R)]
        count = 1
        turn = 0
        if in_grid(R, C, r0, c0):
            r_list.append([r0,c0])
            A[r0][c0] = 1
        while not is_over(A, R, C):
            for i in range(count):
                r0, c0 = go_direction(turn, r0, c0)
                if in_grid(R, C, r0, c0):
                    r_list.append([r0,c0])
                    A[r0][c0] = 1
            turn = (turn + 1) % 4
            if turn % 2 == 0:
                count += 1

        return r_list


        # ---------------- Solution 1 ----------- 

        r_list = []
        re = 0
        count = 1
        turn = 0 
        if in_grid(R, C, r0, c0):
            r_list.append([r0,c0])
            re += 1
        while re != R * C:
            for i in range(count):
                r0, c0 = go_direction(turn, r0, c0)
                if in_grid(R, C, r0, c0):
                    r_list.append([r0,c0])
                    re += 1
            turn = (turn + 1) % 4
            if turn % 2 == 0:
                count += 1

        return r_list
        