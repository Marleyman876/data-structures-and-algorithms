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



if __name__ == "__main__":

    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")

    result = str(ll1)
    print(result)
