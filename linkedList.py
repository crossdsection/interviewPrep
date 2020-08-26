class Node:
    def __init__(self):
        self.value = None
        self.next = None

def find(node, element):
    if node.value == element:
        return True
    elif node.next == None:
        return False
    else :
        return find(node.next, element)


def insert(head, newnode, index):
    if index == 0:
        newnode.next = head
        head = newnode
    else :
        current = head
        for i in range(0,index-1) :
            current = current.next
        newnode.next = current.next
        current.next = newnode
    return head