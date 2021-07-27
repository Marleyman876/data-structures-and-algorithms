import pytest
from code_challenges.trees.trees import Node, BinaryTree, BinarySearchTree


#****************************************************************Binary Tree Tests********************************************************************
#@pytest.mark.skip("pending")
def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"


#@pytest.mark.skip("pending")
def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left is None


#@pytest.mark.skip("pending")
def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right is None


#@pytest.mark.skip("pending")
def test_create_binary_tree():
    tree = BinaryTree()
    assert tree


#@pytest.mark.skip("pending")
def test_binary_tree_has_root():
    tree = BinaryTree()
    assert tree.root is None

def test_tree_root(binary_tree):
    actual = binary_tree.root.value
    expected = 'potato'
    assert actual == expected


#@pytest.mark.skip("pending")
def test_create_binary_search_tree():
    tree = BinarySearchTree()
    assert tree


#************Testing Empty Tree********************
def test_empty_tree_pre_order(empty_tree):
    actual = empty_tree.pre_order()
    expected = "Tree is empty"
    assert actual == expected

def test_empty_tree_post_order(empty_tree):
    actual = empty_tree.post_order()
    expected = "Tree is empty"
    assert actual == expected

def test_empty_tree_in_order(empty_tree):
    actual = empty_tree.in_order()
    expected = "Tree is empty"
    assert actual == expected


def test_pre_order_fruit(binary_tree):
    actual = binary_tree.pre_order()
    expected = ['potato','apple','grape','lychee','rambutan','mangoes','guineps']
    assert actual == expected

def test_in_order(binary_tree):
    actual = binary_tree.in_order()
    expected = ['grape', 'apple', 'lychee', 'potato', 'mangoes', 'rambutan', 'guineps']
    assert actual == expected

def test_post_order(binary_tree):
    actual = binary_tree.post_order()
    expected = ['grape', 'lychee', 'apple', 'mangoes', 'guineps', 'rambutan', 'potato']
    assert actual == expected


def test_add_node_BST():
    bst = BinarySearchTree()
    bst.add(10)
    actual = bst.root.value
    expected = 10
    assert actual == expected

def test_add_empty_node():
    bst = BinarySearchTree()
    actual = bst.add('')
    expected = 'Node must contain Integer'
    assert actual == expected

def test_add_non_int_node():
  tree = BinarySearchTree()
  actual = tree.add("Binary Search Trees is confusing")
  expected = 'Node must contain Integer'
  assert actual == expected


 #****************************Code challenege 16**********************************

def test_max_value(binary_tree_int):
    actual = binary_tree_int.find_max_value()
    expected = 25
    assert actual == expected

def test_max_value(empty_tree):
    actual = empty_tree.find_max_value()
    expected = 'root value cannot be empty'
    assert actual == expected

def test_max_value_fail(binary_tree_int):
    actual = binary_tree_int.find_max_value()
    expected = 13
    assert actual != expected


@pytest.fixture
def empty_tree():
    empty_tree = BinaryTree()
    return empty_tree


@pytest.fixture
def binary_tree():
    tree = BinaryTree()
    tree.root = Node('potato')
    tree.root.left = Node('apple')
    tree.root.left.left = Node('grape')
    tree.root.left.right = Node('lychee')
    tree.root.right = Node('rambutan')
    tree.root.right.left = Node('mangoes')
    tree.root.right.right = Node('guineps')
    return tree


@pytest.fixture
def binary_tree_int():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(5)
    tree.root.right = Node(10)
    tree.root.left.right = Node(25)
    tree.root.left.right.left = Node(13)
    tree.root.left.right.right = Node(15)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    return tree
