"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
"""


from re import L
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):

    seen_nodes = set()

    current = head

    while current:
        if current in seen_nodes:
            return True
        seen_nodes.add(current)
        current = current.next
    return False

# Floyd's Tortoise & Hare algorith.
def hasCycleFTH(head):

    slow = head
    fast = head

    while fast:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def printLinkedList(head):

    while head:
        print(head.val, end="--> ")
        head = head.next
    print("None.")


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next.next


printLinkedList(head)
print(hasCycle(head))
print(hasCycleFTH(head))
