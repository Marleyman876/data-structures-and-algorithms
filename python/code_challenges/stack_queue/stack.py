class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:

    def __init__(self, top=None) -> None:
        self.next = next
        self.top = top

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def is_Empty(self):
        if self.top is None:
         return True
        else:
            return False

    def pop(self):
        if self.is_Empty():
            raise Exception("Stack is empty, cannot pop from empty stack!")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.is_Empty():
            raise Exception('Peeking from an empty stack')
        return self.top.next.value


class 
