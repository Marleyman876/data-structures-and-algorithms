# Problem Domain

Write a function called breadth first that takes in an arguments of a tree.
The function will return a list of all values in the tree in the order they were encountered.

## Edge Cases

Empty tree

## Visual

see .png image in folder

## Big O

Time = O(n)
Space = O(n)

## Algorithm

Define a function that takes in an argument of a tree
Check if tree is empty, handle error
Create access to a list
Create queue
Enqueue the root into a queue
While queue is not empty
Assign variable 'front' to the dequeued root node to have access to it's left and right
Append front to list
Check if left exist, if so enqueue
Check if right exists, if so enqueue
Return the list

## Code

```py

def breadth_first(tree):
    if tree.root is None:
        return 'Tree is empty'
    list = []
    queue = Queue() #queue() is imported from my stack method folder
    queue.enqueue(tree.root)
    while not queue.is_Empty():
        front = queue.dequeue()
        list.append(front.value)

        if front.left:
            queue.enqueue(front.left)
        if front.right:
            queue.enqueue(front.right)

    return list
