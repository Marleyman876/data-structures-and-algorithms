# K-Ary Tree

## Problem Domain

Given a k-ary tree write a function that transforms the tree using fizz buzz.

## Input = Tree

## Output = Transformed Tree

## Edge Cases

1. Empty Tree

2. Empty Array

## Big O

Time: O (n)
Space: O(w) width or O(n)

## Algorithm

* write a fizz buzz function
* initialize queue with root of tree
* using a while loop while the queue is not empty, dequeue the front use a helper function to declare front value and do the calculating
*return the tree

## Code

```py
def fizz_buzz_helper(num):

    if num % 15 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


def fizz_buzz_tree(tree):

    if tree.root is None:
        raise Exception("Tree is empty")

    queue = Queue()
    queue.enqueue(tree.root)


    while not queue.is_Empty():
        front = queue.dequeue()
        front.value = fizz_buzz_helper(front.value)
        for node in front.children:
            queue.enqueue(node)

    return tree
    