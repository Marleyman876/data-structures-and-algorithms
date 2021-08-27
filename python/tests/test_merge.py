from code_challenges.merger_sort.merger import merge_sort, merge



def test_sort():
    int_list = merge_sort([45,67,3,27,13,8])
    expected = [3, 8, 13, 27, 45, 67]
    assert int_list == expected

def test_sort_decimal_negatives():
    int_list = merge_sort([-45,6.7,-3,2.7,.13,8.0])
    expected = [-45, -3, 0.13, 2.7, 6.7, 8.0]
    assert int_list == expected


def test_sort_negatives():
    int_list = merge_sort([-10,-9,-8,-7,-6,-5,-435,-8892])
    expected = [-8892, -435, -10, -9, -8, -7, -6, -5]
    assert int_list == expected


def test_one_item():
    int_list = merge_sort([20])
    expected = [20]
    assert int_list == expected
