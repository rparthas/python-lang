# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.val}"


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next



if __name__ == "__main__":
    four = ListNode(4)
    two = ListNode(2,four)
    one = ListNode(1,two)

    five_2 = ListNode(5)
    three = ListNode(3,five_2)
    one_2 = ListNode(1,three)

    result = Solution().mergeTwoLists(one, one_2)
    node = result
    while node:
        print(node.val)
        node = node.next
