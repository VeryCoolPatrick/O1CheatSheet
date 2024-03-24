from typing import Optional

"""
**EXPLANATION**

Two pointers (SLOW and FAST) are used to traverse through a linked list. FAST will move at twice the speed of SLOW 
(SLOW = 1 node, FAST = 2 nodes).

If a cycle is NOT present:
FAST will eventually reach the end of the list, at which point its value will be NONE (or NULL).

If a cycle is present:
SLOW and FAST will eventually point to the same node. At that point, we reset only one of them to the head of the 
linked list, while the other will maintain its position. We now once again traverse through the list, this time with 
both SLOW and FAST moving at the same speed (1 node at the time). Eventually they will again meet at a specific node, 
which is precisely the starting point of the cycle.
"""


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def tortoise_hare(head: ListNode) -> Optional[ListNode]:
    """
    - Time complexity: O(n)
    - Space complexity: O(1)
    
    :param head: head of the linked list
    :returns: None if no cycle is found, else the node at which the cycle occurs
    """

    slow = fast = head
    met = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            met = True
            break

    if not met:
        return None
    else:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

    return slow
