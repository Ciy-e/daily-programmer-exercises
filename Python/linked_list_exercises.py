#!/bin/python3

class SinglyLinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data
    
    def get_next_node(self):
        return self.next

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

# determines if linked list has a cycle in it.
def has_cycle(head):
    detected_cycle = False
    null_found = False
    cur = head
    node_ids = []
    while not detected_cycle and not null_found:
        node_ids.append(id(cur))
        if not cur.next:
            null_found = True
        elif id(cur.next) in node_ids:
            detected_cycle = True
        else:
            cur = cur.next
            
    return detected_cycle and not null_found

# insert to a doubly linked list that is sorted while maintaining sort.
def sortedInsert(head, data):
    cur = head
    added = False
    
    if data < head.data:
        newNode = DoublyLinkedListNode(data)
        newNode.next = head
        head.prev = newNode
        head = newNode
        added = True

    while not added:
        if not cur.next:
            cur.next = DoublyLinkedListNode(data)
            cur.next.prev = cur
            added = True
        elif data > cur.data and data <= cur.next.data:
            newNode = DoublyLinkedListNode(data)
            newNode.prev = cur
            newNode.next = cur.next
            cur.next.prev = newNode
            cur.next = newNode
            added = True
        else:
            cur = cur.next
    return head