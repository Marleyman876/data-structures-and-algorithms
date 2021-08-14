from code_challenges.linked_list.linked_list import LinkedList, Node, zip_two_lists


#to test empty Linked List
def test_one():
   ll1 = LinkedList()
   actual = ll1.head
   expected = None
   assert actual == expected

def test_two():
    ll2 = LinkedList()
    ll2.insert("a")
    ll2.insert("b")
    actual = ll2.head.value
    expected = "b"
    assert actual == expected

def test_special_character():
    ll_spec = LinkedList()
    ll_spec.insert('!')
    ll_spec.insert('@')
    actual = ll_spec.head.value
    expected = '@'
    assert actual == expected


def test_three():
    node1 = Node("a")
    ll1 = LinkedList(node1)
    actual = ll1.head.value
    excepted = "a"
    assert actual == excepted
def test_four():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c")
    actual = ll1.head.value
    expected = "c"
    assert actual == expected

def test_five():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    actual = ll1.includes("c")
    expected = True
    assert actual == expected

def test_six():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    actual = ll1.includes("x")
    expected = False
    assert actual == expected

def test_seven():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    actual = str(ll1)
    expected = "{'d'} ->{'c'} ->{'b'} ->{'a'} -> None "
    assert actual == expected

def test_append_to_end():
    new_list = LinkedList(Node('1',Node('3',Node('2'))))
    new_list.append_to_end('5')
    actual= new_list.__str__()
    expected = "{'1'} ->{'3'} ->{'2'} ->{'5'} -> None "
    assert actual == expected

def test_insert_before_value():
    new_list = LinkedList(Node('1',Node('3',Node('2'))))
    new_list.insert_before_value('3','5')
    actual = new_list.__str__()
    expected = "{'1'} ->{'5'} ->{'3'} ->{'2'} -> None "
    assert actual == expected

def test_insert_after_value():
    new_list = LinkedList(Node('1',Node('3',Node('2'))))
    new_list.insert_after_value('3','5')
    actual = new_list.__str__()
    expected = "{'1'} ->{'3'} ->{'5'} ->{'2'} -> None "
    assert actual == expected

# k is greater than length of list

def test_from_end():
    new_list = LinkedList(Node(1,Node(3,Node(8, Node(2)))))
    expected = 2
    actual = new_list.from_end(0)
    assert actual == expected

def test_from_end_negative_number():
    new_list = LinkedList(Node(1,Node(3,Node(8, Node(2)))))
    expected = "negative Number"
    actual = new_list.from_end(-1)
    assert actual == expected

def test_from_end_same_length():
    new_list = LinkedList(Node(1,Node(3,Node(8, Node(2)))))
    expected = "Same Length"
    actual = new_list.from_end(4)
    assert actual == expected

def test_from_end_out_of_range():
    new_list = LinkedList(Node(1,Node(3,Node(8, Node(2)))))
    expected = "Out of Range"
    actual = new_list.from_end(7)
    assert actual == expected

def test_from_end_greater_than_1():
    new_list = LinkedList(Node(1))
    expected = 1
    actual = new_list.from_end(0)
    assert actual == expected

def test_from_end_middle_of_list():
    new_list = LinkedList(Node(1,Node(3,Node(8, Node(2)))))
    expected = 3
    actual = new_list.from_end(2)
    assert actual == expected


def test_zip_two_lists():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append_to_end("a").append_to_end("c").append_to_end("e")
    ll2.append_to_end("b").append_to_end("d").append_to_end("f")
    actual = zip_two_lists(ll1,ll2)
    expected = "{'a'} ->{'b'} ->{'c'} ->{'d'} ->{'e'} ->{'f'} -> None "
    assert str(actual) == expected
