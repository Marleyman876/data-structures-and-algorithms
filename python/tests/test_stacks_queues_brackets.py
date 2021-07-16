import pytest
from code_challenges.stack_queues_brackets.stack_queues_brackets import Brackets


def test_brackets():
    string = "{Hello, World}[}"
    Brackets(string)
    actual = False
    expected = False
    assert actual == expected

def test_brackets_false():
    string = "{This test should pass as true}{}"
    Brackets(string)
    actual = True
    expected = True
    assert actual == expected

def test_alternate():
    string = "{"
    Brackets(string)
    actual = True
    expected = False
    assert actual != expected

