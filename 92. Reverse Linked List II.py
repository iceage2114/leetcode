
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):

    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    current = prev.next
    previous = None
    for i in range(right - left + 1):
        next = current.next
        current.next = previous
        previous = current
        current = next

    prev.next.next = current
    prev.next = previous

    return dummy.next

