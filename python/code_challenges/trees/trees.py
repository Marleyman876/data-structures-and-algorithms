
from code_challenges.stack_queue.stack import Queue, Node



class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    pass

class BinaryTree:
    def __init__(self, root=None):
        self.root = root


    def pre_order(self):
        # root >> left >> right
        if self.root == None:
            return 'Tree is empty'
        tree_order = []

        def pre_order_traverse(root):
            tree_order.append(root.value)

            if root.left != None:
                pre_order_traverse(root.left)

            if root.right != None:
                pre_order_traverse(root.right)

        pre_order_traverse(self.root)
        return tree_order

    def in_order(self):
        # left >> root >> right
        if self.root == None:
            return 'Tree is empty'

        tree = []
        def in_order_traverse(root):

            if root.left != None:
                in_order_traverse(root.left)
            tree.append(root.value)
            if root.right != None:
                in_order_traverse(root.right)

        in_order_traverse(self.root)
        return tree

    def post_order(self):
        # left >> right >> root
        if self.root == None:
            return 'Tree is empty'

        tree_post_order = []

        def traverse_post_order(root):

            if root.left != None:
                traverse_post_order(root.left)

            if root.right != None:
                traverse_post_order(root.right)

            tree_post_order.append(root.value)

        traverse_post_order(self.root)

        return tree_post_order

    #****************************Code challenege 16**********************************

    def find_max_value(self):
        if (self.root == None):
            return 'root value cannot be empty'

        all_values = self.post_order()
        max_value = all_values[0]

        for i in all_values:
            if i > max_value:
                max_value = i

        return max_value

#****************************Code challenege 17**********************************

    # def breadth_first(self):
    #     root = self.root

    #     if root is None:
    #       return 'Tree is empty'
    #     else:
    #         list = []
    #         queue = Queue() #queue() is imported from my stack method folder
    #         queue.enqueue(root)

    #     while not queue.is_Empty():
    #         front = queue.dequeue()
    #         list.append(front.value)

    #         if front.left:
    #             queue.enqueue(front.left)
    #         if front.right:
    #           queue.enqueue(front.right)

    #     return list




class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
      self.root = root

    def add(self, value):
       new_node = Node(value)

       if self.root is None:
        self.root = new_node

        current = self.root
        if value != None or type(value) == str:
            return 'Node must contain Integer'


        while current != None:
            if current.value > value:
                if current.left is None:
                    current.left = new_node
                else:
                    current = current.left

            elif current.value < value:
                if current.right is None:
                    current.right = new_node
                else:
                    current = current.right

            if current.value == value:
                return 'Value is already in the tree'


    def contains(self, value):
        current = self.root
        while current is not None:
            if current.value > value:
                current = current.left
            if current.value < value:
                current = current.right
            if current.value == value:
                return True
            else:
                return False



