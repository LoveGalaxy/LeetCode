"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ---------------- Solution 0 -----------
        without_re_s = ""
        max_s = 0
        for c in s:
            if c not in without_re_s:
                without_re_s += c
            else:
                max_s = max(max_s, len(without_re_s))
                without_re_s = without_re_s.split(c)[-1] + c
        return max(max_s, len(without_re_s))
