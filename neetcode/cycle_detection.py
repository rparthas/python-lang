# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fp = head
        sp = head
        start = True
        while fp is not None and sp is not None:
            if not start and fp.val == sp.val:
                return True
            start = False
            sp = sp.next
            fp = fp.next
            if fp is not None:
                fp = fp.next
        return False

        #        seen = set()
        #        node = head
        #        while node.next is not None:
        #            if node.val in seen:
        #                return True
        #            seen.add(node.val)
        #            node = node.next
        #        return False


if __name__ == "__main__":
    two = ListNode(2)
    one = ListNode(1)
    four = ListNode(4)
    three = ListNode(3)
    one.next = two
    two.next = three
    three.next=four
    four.next = one
    print(Solution().hasCycle(one))
