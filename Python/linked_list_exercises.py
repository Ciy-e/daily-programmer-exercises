#!/bin/python3

#prints the entire linked list given the head node.
def printLinkedList(head):
    cur = head
    while cur:
        print(cur.data)
        cur=cur.next
