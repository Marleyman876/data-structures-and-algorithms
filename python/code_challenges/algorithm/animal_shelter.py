import copy


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


"""
animal object
{
    animal: "dog"
}
"""


class Animal_Shelter:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, obj):

        node = Node(obj)

        if self.front is None:
            self.front = node
            self.rear = node
            return self

        self.rear.next = node
        self.rear = node
        self.length += 1
        return self

    def dequeue(self, pref):

        if self.front is None:
            raise Exception("Queue is Empty")

        if self.front.value["animal"] == pref:
            dequed = self.front.value["animal"]
            self.front = self.front.next
            self.length -= 1
            return dequed

        temp_length = copy.deepcopy(self.length)
        answer = None

        while temp_length >= 0:
            if self.front.value["animal"] == pref:
                answer = self.front.value["animal"]
                self.front = self.front.next
                self.length -= 1
                temp_length -= 1
                break
            else:
                dequed = self.front.value
                dequed_node = Node(dequed)
                self.front = self.front.next
                self.rear.next = dequed_node
                self.rear = dequed_node
                temp_length -= 1

        for i in range(temp_length + 1):
            dequed = self.front.value
            dequed_node = Node(dequed)
            self.front = self.front.next
            self.rear.next = dequed_node
            self.rear = dequed_node

        return answer
