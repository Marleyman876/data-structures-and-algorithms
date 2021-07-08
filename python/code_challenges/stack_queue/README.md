# Code Challenge : Class 10 Stacks and Queues

## Stack Tasks

1. Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue.

2. Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

3. Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    This object should be aware of a default empty value assigned to top when the stack is created.
    The class should contain the following methods:

    * push
    Arguments: value
    adds a new node with that value to the top of the stack with an O(1) Time performance.

    * pop
    Arguments: none
    Returns: the value from node from the top of the stack
    Removes the node from the top of the stack
    Should raise exception when called on empty stack

    * peek
    Arguments: none
    Returns: Value of the node located at the top of the stack
    Should raise exception when called on empty stack

    * is empty
    Arguments: none
    Returns: Boolean indicating whether or not the stack is empty.

## Queues Task

1. Create a Queue class that has a front property. It creates an empty Queue when instantiated.

    * This object should be aware of a default empty value assigned to front when the queue is created.

2. The class should contain the following methods:

    * enqueue
    Arguments: value
    adds a new node with that value to the back of the queue with an O(1) Time performance.

    * dequeue
    Arguments: none
    Returns: the value from node from the front of the queue
    Removes the node from the front of the queue
    Should raise exception when called on empty queue

    * peek
    Arguments: none
    Returns: Value of the node located at the front of the queue
    Should raise exception when called on empty stack

    * is empty
    Arguments: none
    Returns: Boolean indicating whether or not the queue is empty

## Write tests to prove the following functionality:

[x] Can successfully push onto a stack
[x] Can successfully push multiple values onto a stack
[x] Can successfully pop off the stack
[x] Can successfully empty a stack after multiple pops
[x] Can successfully peek the next item on the stack
[x] Can successfully instantiate an empty stack
[x] Calling pop or peek on empty stack raises exception
[x] Can successfully enqueue into a queue
[x] Can successfully enqueue multiple values into a queue
[x] Can successfully dequeue out of a queue the expected value
[x] Can successfully peek into a queue, seeing the expected value
[x] Can successfully empty a queue after multiple dequeues
[x] Can successfully instantiate an empty queue
[x] Calling dequeue or peek on empty queue raises exception

<!-- ####################Code Challenge 11############## -->

## Stacks Queue Psuedo [Collaboraed with Wondwosen]

* Create a new class called pseudo queue
* Do not use an existing Queue.
* Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),

* Internally, utilize 2 Stack instances to create and manage the queue

## Methods

* enqueue
Arguments: value
Inserts value into the PseudoQueue, using a first-in, first-out approach.

* dequeue
Arguments: none
Extracts a value from the PseudoQueue, using a first-in, first-out approach.

[White Board](code_challenges/stack_queue/stack-queue-pseudo.jpg)
