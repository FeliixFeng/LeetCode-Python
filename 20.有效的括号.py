#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 右括号 -> 对应的左括号
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []

        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False

            else:
                stack.append(ch)
            
        
        return not stack
        
# @lc code=end

