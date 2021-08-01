import pytest
from code_challenges.stack_queue.stack import Stack,Node,Queue,PseuedoQueue

def test_push_stack():
    new_stack = Stack()
    new_stack.push(4)
    actual = new_stack.top.value
    expected = 4
    assert actual == expected

def test_push_stack():
    new_stack = Stack()
    new_stack.push(4)
    new_stack.push(3)
    new_stack.push(2)
    new_stack.push(1)

    actual_top = new_stack.top.value
    expected_top = 1

    actual_second = new_stack.top.next.value
    expected_second = 2

    actual_third = new_stack.top.next.next.value
    expected_third = 3

    actual_fourth = new_stack.top.next.next.next.value
    expected_fourth = 4

    assert actual_top == expected_top
    assert actual_second == expected_second
    assert actual_third == expected_third
    assert actual_fourth == expected_fourth

def test_empty_stack():
    new_stack = Stack()
    actual = new_stack.is_Empty()
    expected = True
    assert actual == expected

def test_pop_stack():
    new_stack = Stack()
    new_stack.push(4)
    new_stack.push(3)
    new_stack.push(2)
    new_stack.push(1)
    new_stack.pop()
    actual = new_stack.top.value
    expected = 2
    assert actual == expected

def test_peek():
    new_stack = Stack()
    new_stack.push(4)
    new_stack.push(3)
    new_stack.push(2)
    new_stack.push(1)
    new_stack.peek()
    actual = new_stack.top.value
    expected = 1
    assert actual == expected

#####################################QUEUES#########################################

def test_empty_queue():
    new_queue = Queue()
    actual = new_queue.is_Empty()
    expected = True
    assert actual == expected

def test_add_que():

        new_que = Queue()

        new_que.enqueue('E')
        new_que.enqueue('M')
        new_que.enqueue('B')
        new_que.enqueue('R')
        new_que.enqueue('A')
        new_que.enqueue('C')
        new_que.enqueue('E')
        new_que.enqueue('-')
        new_que.enqueue('T')
        new_que.enqueue('H')
        new_que.enqueue('E')
        new_que.enqueue('-')
        new_que.enqueue('S')
        new_que.enqueue('U')
        new_que.enqueue('C')
        new_que.enqueue('K')

        actual = new_que.back.value
        expected  = 'K'

        assert actual == expected


def test_deque():
    new_queue = Queue()
    new_queue.enqueue('p')
    new_queue.enqueue('y')
    new_queue.enqueue('t')
    new_queue.enqueue('h')
    new_queue.enqueue('o')
    new_queue.enqueue('n')
    actual = new_queue.dequeue()
    expected = 'p'
    assert actual == expected

def test_peek():
    new_queue = Queue()
    new_queue.enqueue('p')
    new_queue.enqueue('y')
    new_queue.enqueue('t')
    new_queue.enqueue('h')
    new_queue.enqueue('o')
    new_queue.enqueue('n')
    actual = new_queue.peek()
    expected = 'p'
    assert actual == expected


# Challlenge 11

def test_can_instantiate_a_new_PseuedoQueue_class():
    new_pseudo = PseuedoQueue()
    actual_1 = new_pseudo.stack_1.top
    actual_2 = new_pseudo.stack_2.top
    expected_1 = None
    expected_2 = None
    assert actual_1 == expected_1
    assert actual_2 == expected_2


def test_can_succefully_enqueue_one_value():
    new_pseudo = PseuedoQueue()
    new_pseudo.enqueue("a")
    actual = new_pseudo.stack_1.top.value
    expected = "a"
    assert actual == expected

def test_can_succesfully_enqueue_multiple_values(new_pseudo):
    actual_1 = new_pseudo.stack_1.top.value
    expected_1 = "d"
    actual_2 = new_pseudo.stack_1.top.next.value
    expected_2 = "c"
    assert actual_1 == expected_1
    assert actual_2 == expected_2

def test_dequeue_one_node(new_pseudo):
    actual = new_pseudo.dequeue()
    expected = "a"
    assert actual == expected

def test_can_succesfully_dequeue_until_empty(new_pseudo):
    while not new_pseudo.is_Empty():
        new_pseudo.dequeue()
    assert new_pseudo.stack_1.is_Empty()

def test_dequeeing_an_empty_queue_will_raise_exception():
    empty_pseudo = PseuedoQueue()
    with pytest.raises(Exception):
        empty_pseudo.dequeue()
######################
# Fixtures
######################
@pytest.fixture
def new_pseudo():
    new_pseudo = PseuedoQueue()
    new_pseudo.enqueue("a")
    new_pseudo.enqueue("b")
    new_pseudo.enqueue("c")
    new_pseudo.enqueue("d")
    return new_pseudo
@pytest.fixture(autouse=True)
def clean():
    """runs before each test automatically
    There's also a more advanced way to run code after each test as well
    Check the docs for that. Hint: it uses yield
    """
    new_pseudo = None
