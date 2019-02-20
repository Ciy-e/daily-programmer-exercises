#!/bin/python3

#prints the entire linked list given the head node.
def printLinkedList(head):
    cur = head
    while cur:
        print(cur.data)
        cur=cur.next

# inserts a node at the given index of a singly linked list and returns a pointer to the head of the new list.
def insertNodeAtPosition(head, data, position):
    cur = head
    newNode = SinglyLinkedListNode(data)
    added = False
    ctr = 0
    if position == 0:
        newNode.next = head
        head = newNode
        added = True
    while not added and cur:
        if ctr == position-1:
            newNode.next = cur.next
            cur.next = newNode
            added = True
        cur=cur.next
        ctr+=1
    return head

# reverses a linked list
def reverse(head):
    s = []
    cur = head
    while cur:
        s.append(cur.data)
        cur=cur.next
    cur = head
    while cur:
        cur.data = s.pop()
        cur=cur.next
    return head