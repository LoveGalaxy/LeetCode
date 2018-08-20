"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        # ---------------- Solution 0 -----------
        l = len(post)
        if l == 0:
            return None
        root = TreeNode(pre[0])
        if l == 1:
            return root
        else:

            i = pre.index(post[-2])
            root.left = self.constructFromPrePost(pre[1:i], post[0:i-1])
            root.right = self.constructFromPrePost(pre[i:], post[i-1:-1])
        return root