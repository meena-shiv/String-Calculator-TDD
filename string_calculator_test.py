import pytest
from string_calculator import add

def test_add_empty_string():
    assert add("") == 0

def test_add_single_number():
    assert add("1") == 1

def test_add_two_numbers():
    assert add("1,2") == 3

def test_add_multiple_numbers():
    assert add("1,2,3,4,5") == 15

def test_add_newline_delimiters():
    assert add("1\n2,3") == 6

def test_add_custom_delimiter():
    assert add("//;\n1;2") == 3

def test_add_negative_numbers():
    try:
        add("1,-2,3,-3")
    except ValueError as e:
        assert str(e) == "negative numbers not allowed -2, -3"
    else:
        pytest.fail("ValueError not raised")

def test_ignore_numbers_greater_than_1000():
    assert add("2,1001") == 2
    assert add("1000,999,1001") == 1999

def test_custom_delimiters_of_any_length():
    assert add("//[***]\n1***2***3") == 6
    assert add("//[---]\n4---5---6") == 15

def test_multiple_custom_delimiters():
    assert add("//[*][%]\n1*2%3") == 6
    assert add("//[+][-]\n4+5-6") == 15

