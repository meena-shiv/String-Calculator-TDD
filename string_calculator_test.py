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
