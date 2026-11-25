#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for word in strs:
            sorted_chars = sorted(word)
            key = "".join(sorted_chars)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)
        return list(groups.values())

# @lc code=end
