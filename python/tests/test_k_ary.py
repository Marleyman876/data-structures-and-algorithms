import pytest

from code_challenges.trees.k_tree.k_tree import KNodes, KaryTree, fizz_buzz_helper, fizz_buzz_tree


def test_can_instantiate_kary_node():
    node = KNodes(3)
    assert node.value == 3
    assert node.children == []

# def empty_tree():
#     empty_tree = new_tree()
#     return empty_tree

def test_can_instantiate_empty_kary_tree():
    new_kary = KaryTree()
    assert new_kary.root == None


def test_can_instantiate_kary_tree_with_one_node():
    knode = KNodes(10, [1, 2, 3, 4])
    new_kary = KaryTree(knode)
    assert new_kary.root.value == 10
    assert new_kary.root.children == [1, 2, 3, 4]


def test_Kary_tree_breadth_first_returns_correct_values(new_tree):
    actual = new_tree.breadth_first()
    expected = [1, 2, 3, 4, 5, 11, 6, 7, 10, 8, 9]
    assert actual == expected


def test_fizz_buzz_helper_returns_fizz(new_tree):
    pass


def test_fizz_buzz_helper_returns_buzz():
    pass


def test_fizz_buzz_helper_returns_fizzbuzz():
    pass


def test_fizz_buzz_helper_returns_string():
    pass


def test_fizz_buzz_tree_raises_error_on_empty_tree():
    pass


def test_fizz_buzz_tree_return_corrrect_values(new_tree):
    modified = fizz_buzz_tree(new_tree)
    actual = modified.breadth_first()
    expected = ["1", "2", "Fizz", "4", "Buzz", "11", "Fizz", "7", "Buzz", "8", "Fizz"]
    assert actual == expected


@pytest.fixture
def new_tree():
    node5 = KNodes(5, [])
    node6 = KNodes(6, [])
    node7 = KNodes(7, [])
    node8 = KNodes(8, [])
    node9 = KNodes(9, [])
    node10 = KNodes(10, [])
    node11 = KNodes(11, [])
    node4 = KNodes(4, [node8, node9])
    node2 = KNodes(2, [node4, node5, node11])
    node3 = KNodes(3, [node6, node7, node10])
    node1 = KNodes(1, [node2, node3])
    new_tree = KaryTree(node1)
    return new_tree



















