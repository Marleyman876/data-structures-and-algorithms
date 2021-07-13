import pytest

from code_challenges.algorithm.animal_shelter import Animal_Shelter


def test_node_class_can_instantiate():
    pass


def test_can_Animal_shelter_instantiate():
    new_shelter = Animal_Shelter()
    assert new_shelter.front == None
    assert new_shelter.rear == None
    assert new_shelter.length == 0


def test_can_enqueue_animal_object_into_Animal_shelter():
    new_shelter = Animal_Shelter()
    input1 = {"animal": "dog"}
    new_shelter.enqueue(input1)
    assert new_shelter.front.value["animal"] == "dog"
    assert new_shelter.rear.value["animal"] == "dog"


def test_can_dequeue_animal_from_Animal_shelter():
    new_shelter = Animal_Shelter()
    input1 = {"animal": "dog"}
    input2 = {"animal": "cat"}
    new_shelter.enqueue(input1)
    new_shelter.enqueue(input2)
    actual = new_shelter.dequeue("dog")
    expected = "dog"
    assert actual == expected
    assert new_shelter.front.value["animal"] == "cat"


def test_can_dequeue_animal_from_Animal_shelter():
    new_shelter = Animal_Shelter()
    input1 = {"animal": "dog"}
    input2 = {"animal": "dog"}
    input3 = {"animal": "cat"}
    input4 = {"animal": "dog"}
    input5 = {"animal": "cat"}
    new_shelter.enqueue(input1)
    new_shelter.enqueue(input2)
    new_shelter.enqueue(input3)
    new_shelter.enqueue(input4)
    new_shelter.enqueue(input5)
    actual = new_shelter.dequeue("cat")
    expected = "cat"
    assert actual == expected
    assert new_shelter.front.value["animal"] == "dog"
    assert new_shelter.rear.value["animal"] == "cat"
