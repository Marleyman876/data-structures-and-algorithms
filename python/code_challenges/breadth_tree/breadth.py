from code_challenges.stack_queue.stack import Queue

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

