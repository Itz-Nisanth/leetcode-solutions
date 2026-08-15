'''
Q14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.'''

class Solution(object):
    def longestCommonPrefix(self, strs):

        p = strs[0]
        for i in range(1, len(strs)):
            st = ""
            for j in range(min(len(p), len(strs[i]))):
                if p[j] == strs[i][j]:
                    st = st + strs[i][j]
                else:
                    break
            p = st

        return p
    
s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(s.longestCommonPrefix(["dog","racecar","car"]))  # Output: ""