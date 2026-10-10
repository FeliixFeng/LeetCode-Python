#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            

        return prev
        
# @lc code=end

