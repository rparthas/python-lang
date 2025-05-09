# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.val},{self.next}"

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = curr = head
        while curr and curr.next:
            prev = new_head
            new_head = curr.next
            curr.next,new_head.next= new_head.next,prev


        return new_head



if __name__ == "__main__":
    four = ListNode(4)
    two = ListNode(2,four)
    one = ListNode(1,two)



    result = Solution().reverseList(one)
    print(result)
