from code_challenges.stack_queue.stack import Stack,Node,Queue

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
    expected = 'y'
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
