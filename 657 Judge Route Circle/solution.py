"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # ---------------- Solution 0 ----------- 
        count_U = 0
        count_D = 0
        count_R = 0
        count_L = 0
        for c in moves:
            if c == "U":
                count_U += 1
            elif c == "D":
                count_D += 1
            elif c == "R":
                count_R += 1
            else:
                count_L += 1
        if count_U == count_D and count_R == count_L:
            return True
        return False