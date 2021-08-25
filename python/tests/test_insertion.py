import pytest
from code_challenges.insertions_sort.insert import insertion_sort


def test_sort():
    int_list = [45,67,3,27,13,8]
    insertion_sort(int_list)
    expected = [3, 8, 13, 27, 45, 67]
    assert int_list == expected

def test_sort_decimal_negatives():
    int_list = [-45,6.7,-3,2.7,.13,8.0]
    insertion_sort(int_list)
    expected = [-45, -3, 0.13, 2.7, 6.7, 8.0]
    assert int_list == expected


def test_sort_negatives():
    int_list = [-10,-9,-8,-7,-6,-5,-435,-8892]
    insertion_sort(int_list)
    expected = [-8892, -435, -10, -9, -8, -7, -6, -5]
    assert int_list == expected


def test_expected_to_fail():
    int_list = [20,9,3,-42,6,-1]
    insertion_sort(int_list)
    expected = [-42,-1,4,20,6,3]
    assert int_list != expected
