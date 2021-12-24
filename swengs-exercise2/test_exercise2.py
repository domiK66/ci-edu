import pytest
import traceback

from stack_classes import PositiveNumberStack, NegativeNumberStack

def test_push_stack():
    my_stack = PositiveNumberStack()
    my_stack.push(32)
    assert my_stack.size() == 1
    my_stack.push(47)
    assert my_stack.size() == 2

def test_pop_stack():
    my_stack = PositiveNumberStack()
    my_stack.push(32)
    assert my_stack.size() == 1
    my_stack.pop()
    assert my_stack.size() == 0

def test_pop_return_value():
    my_stack = PositiveNumberStack()
    my_stack.push(32)
    assert my_stack.size() == 1
    assert my_stack.pop() == 32

def test_pop_on_empty_stack():
    my_stack = PositiveNumberStack()
    with pytest.raises(ValueError):
        my_stack.pop()

def test_push_negative_number():
    my_stack = PositiveNumberStack()
    with pytest.raises(ValueError):
        my_stack.push(-1)

def test_max_size():
    my_stack = PositiveNumberStack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    with pytest.raises(ValueError):
        my_stack.push(4)

def test_str_method():
    my_stack = PositiveNumberStack()
    my_stack.push(1)
    assert str(my_stack) == "Stack with 1 object(s)"

def test_push_positive_number():
    my_stack = NegativeNumberStack()
    with pytest.raises(ValueError):
        my_stack.push(1)
    my_stack.push(-1)
    my_stack.push(-2)
    my_stack.push(-3)
    assert my_stack.pop() == -3
    assert my_stack.pop() == -2
    assert my_stack.pop() == -1
    with pytest.raises(ValueError):
        assert my_stack.pop() == 0
    assert str(my_stack) == "Stack with 0 object(s)"