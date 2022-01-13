"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    # base case

    if list1 == None:
        return list2

    if list2 == None:
        return list1

    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
    else:
        list2.next = mergeTwoLists(list1, list2.next)

    if list1.val <= list2.val:
        return list1

    else:
        return list2




head_1 = ListNode(1)
head_1.next = ListNode(2)
head_1.next.next = ListNode(4)

head_0 = ListNode(1)
head_0.next = ListNode(3)
head_0.next.next = ListNode(4)

merge_head = mergeTwoLists(head_1, head_0)
