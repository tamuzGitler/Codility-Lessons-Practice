# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow, fast = head, head
        while (fast and fast.next):

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    l  = ListNode(1)
    head = l
    l.next = ListNode(2)
    l = l.next
    l.next = ListNode(3)
    l = l.next
    l.next = head
    sol = Solution()
    print(sol.hasCycle(head))