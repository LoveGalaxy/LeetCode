"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
# ---------------- Solution 0 ----------- 
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def find_str(i, j, string, strs):
            count = len(strs)
            for s in strs:
                if string == s[i:j]:
                    count -= 1
            return count == 0

        lst = []

        if "" in strs or strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]

        min_string_l = max(len(string) for string in strs)
        min_string = ""
        for string in strs:
            if len(string) <= min_string_l:
                min_string = string
                min_string_l = len(min_string)
        max_s = ""
        for j in range(len(min_string)+1):
            if find_str(0, j, min_string[0:j], strs):
                max_s = min_string[0:j]
        return max_s
                