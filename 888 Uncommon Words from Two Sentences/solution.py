"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
 

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        # ---------------- Solution 0 ----------- 
        head = ListNode(-1)
        lst = []
        dict_A = {}
        dict_B = {}
        list_A = A.split(' ')
        list_B = B.split(' ')
        for word in list_A:
            try:
                dict_A[word] += 1
            except:
                if word != '':
                    dict_A[word] = 1

        for word in list_B:
            try:
                dict_B[word] += 1
            except:
                if word != '':
                    dict_B[word] = 1

        for key in dict_A:
            if dict_A[key] == 1:
                if key not in dict_B:
                    lst.append(key)

        for key in dict_B:
            if dict_B[key] == 1:
                if key not in dict_A:
                    lst.append(key)

        return lst