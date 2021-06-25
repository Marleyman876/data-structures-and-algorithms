class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self, Node=None):
        self.head = Node

    #To insert @ head
    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        return self

    #Takes a value as an argument and returns Boolean

    def includes(self, value):

        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):

        string_value = ""
        current = self.head
        while current is not None:
            string_value += f"{ {current.value} } ->"
            current = current.next

        string_value += f" None "
        return string_value

 ### Code Challenge 5
    def __str__(self):
        string_value = ""
        current = self.head

        while current is not None:
            string_value += f"{ {current.value} } ->"
            current = current.next

        string_value += f" None "
        return string_value

    def append_to_end(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def insert_before_value(self, target, value):
        node_head = self.head
        while node_head.next != None:
            if target == node_head.next.value:
                break
            node_head = node_head.next
        if node_head == None:
            print('No node/value found')
        else:
            new_node = Node(value)
            new_node.next = node_head.next
            node_head.next = new_node

    def insert_after_value(self, target, value):
        # new_node = Node(self,target, value)
        node_head = self.head
        while node_head.next != None:
            if target == node_head.value:
                break
            node_head = node_head.next
        if node_head == None:
            print('No node/value found')
        else:
            new_node = Node(value)
            new_node.next = node_head.next
            node_head.next = new_node

    def from_end(self, k):
        list_head = self.head
        count = 0
        while list_head != None:
           list_head = list_head.next
           count += 1
        if k > count:
            return("Out of Range")
        elif k == count:
            return("Same Length")
        elif k < 0:
            return("negative Number")
        elif k == self:
            return("Linked list needs to be greater than 1")
        list_head = self.head
        for i in range(1,count - k):
            list_head = list_head.next
        return list_head.value


if __name__ == "__main__":

    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")

    result = str(ll1)
    print(result)
