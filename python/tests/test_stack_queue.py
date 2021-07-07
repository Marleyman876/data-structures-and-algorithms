from code_challenges.stack_queue.stack import Stack,Node

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
