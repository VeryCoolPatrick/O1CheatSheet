# Floyd's tortoise and hare

## Usage

Cycle detection in linked lists.

## Explanation

Two pointers (`SLOW` and `FAST`) are used to traverse through a linked list. `FAST` will move at twice the speed of `SLOW` (2 nodes at the time, instead of 1).

- If a cycle is **not** present:  
   `FAST` will eventually reach the end of the list, at which point its value will be **Null**.

- If a cycle is present:  
   `SLOW` and `FAST` will eventually point to the same node. At that point, we reset the position of only one of them to the head of the linked list, while the other will maintain its current position.  
   We now once again traverse through the list, this time with both `SLOW` and `FAST` moving at the same speed (1 node at the time). Eventually they will again meet at a specific node, which is precisely the starting point of the cycle.

## Complexity

- Time complexity: $\mathcal{O}(1)$
- Space complexity: $\mathcal{O}(1)$

## Code (Python)

```python
def tortoise_hare(head: ListNode) -> Optional[ListNode]:
    """
    :param head: head of the linked list.
    :returns: None if no cycle is found, else the node at which the cycle occurs.
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
```
