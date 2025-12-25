
"""

     Problem condition in leetcode: https://leetcode.com/problems/maximum-substrings-with-distinct-start/

"""

class Solution(object):
    def maxDistinct(self, s):
        return len(set(s))