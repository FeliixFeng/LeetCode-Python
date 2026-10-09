#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = tail = ListNode()

        while list1 and list2 : 

            if list1.val > list2.val:
                tail.next = ListNode(list2.val)
                list2 = list2.next
                tail = tail.next
            else:
                tail.next = ListNode(list1.val)
                list1 = list1.next
                tail = tail.next

        tail.next = list1 or list2
            

        return dummy.next
        
# @lc code=end

