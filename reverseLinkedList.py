"""
Given the head of a singly linked list, reverse the list, 
and return the reversed list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    
    prev = None
    current = head


    while current:

        temp_next = current.next

        current.next = prev
        prev = current
        current = temp_next
    
    return prev


def reverseListRecusrively(head):

    if not head:
        return None

    newHead = head

    if head.next:
        newHead = reverseListRecusrively(head.next)
        head.next.next = head
    
    head.next = None

    return newHead

def printLinkedList(head):

    while head:
        print(head.val, end="--> ")
        head = head.next
    print("None.")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

printLinkedList(reverseListRecusrively(head))


