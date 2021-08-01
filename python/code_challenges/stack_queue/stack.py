class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:

    def __init__(self, top=None):
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


class Queue:

    def __init__(self,front=None,back=None):
        self.next = next
        self.front = None
        self.back = None


    def is_Empty(self):
        if self.front == None:
            return True
        else:
            return False

    def enqueue(self, value):
        new_queue = Node(value)
        if self.is_Empty():
            self.front = new_queue
            self.back = new_queue
        else:
            self.back.next = new_queue
            self.back = new_queue


    def dequeue(self):
        if self.is_Empty():
            raise Exception('You cannot deque from an empty queue')
        temp = self.front
        self.front = temp.next
        return temp.value


    def peek(self):
        if self.is_Empty():
            raise Exception('Peeking from an empty queue')
        return self.front.value


#Challenge 11

class PseuedoQueue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, value):
        self.stack_1.push(value)


    def dequeue(self):
        if self.stack_1.is_Empty():
            raise Exception("PseudoQueue is empty")
        while not self.stack_1.is_Empty():
            temp = self.stack_1.pop()
            self.stack_2.push(temp)
        dequed = self.stack_2.pop()
        while not self.stack_2.is_Empty():
            popped = self.stack_2.pop()
            self.stack_1.push(popped)
        return dequed

    def is_Empty(self):
        return self.stack_1.is_Empty()
if __name__ == "__main__":
    pass
