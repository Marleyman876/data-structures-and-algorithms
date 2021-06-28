# Code Challenge 6

## ![White Board](.code_challenge6.png/)

## Problem Domain

Create 3 methods for the linked list that can:
.append(value)
.insertbefore(value, newval)
.insertafter(value, newval)

## Edge Cases

* Empty List

## Input/Output

Input: value in position were it should be inserted/added
Output: new linked list with value in correct position

## Visual

.append(value)
head -> [1] -> [3] -> [2] -> X   {insert 5 at position x}    output  =  head -> [1] -> [5] -> [3] -> [2] -> [5]

.insertbefore(1, 5)
head -> [1] -> [3] -> [2] -> X   {insert 5 before numer 1}   output  =   head -> [5] -> [1] -> [3] -> [2] -> X

.insertafter(3,5)
head -> [1] -> [3] -> [2] -> X {insert 5 after number3}   output = head -> [1] -> [3] -> [5] -> [2] -> X

## Big O

Time: O(n)
Space: O(n)

## Algorithm

Write a fx that can append(value) a node to the of the linked list.
Write a function called insert_before(value, newvalue):  that can insert a value to the given position of the node.
Write a function called insert_after(value, newvalue):  that can insert a value to the given position of the node.

## Pseudo Code

Algorithm:

Write a fx that can append(value) a node to the of the linked list.
Write a function called insert_before(value, newvalue):  that can insert a value to the given position of the node.
Write a function called insert_after(value, newvalue):  that can insert a value to the given position of the node.

## Code

.append(value):

def append(self, value):
    current = self.head
   While current.next != None:
    current = current.get.next
current.setnext(Node(value))
Return list name.__str__

.insertbefore(value, newvalue):

def insertbefore(self, value, newvalue):
   new_node = Node(value)  # create a new node once we are ready to return the LL
   current_node = self.head
 If current_node = None:
print(The list is empty)
   if current_node.next == value:
Current_node = new_node
   else:
 Current_node = current_node.next

    return new_node

.insertafter(value, newvalue):code challenege 7

def insertafter(self, value, newvalue):
   new_node = Node(value)  # create a new node once we are ready to return the LL
   current_node = self.head
 If current_node = None:
print(The list is empty)
   if current_node == value
Current_node.next = new_node
   else:
 Current_node = current_node.next

    return new_node

## Verification

## Challenge #7

### Problem Domian

Write the following method for the Linked List class:

kth from end
argument: a number, k, as a parameter.
Return the node’s value that is k places from the tail of the linked list.
You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Edge Cases

* If list is empty return None
* number not present in LL

## Visual

ll= [[1][2][3][4][5]], 2

Output = 3

## Big O
Time <--O(n)
Space <--O(1)

## Algorithm

Define a function that takes in a LL and a number k.
If ll is empty return none
Return the node’s value that is k places from the tail of the linked list.You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Code

```py
Code

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
```

** Got some help from Anthony Beaver [TA] on this challenge

