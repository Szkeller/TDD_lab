import pytest

def add(x,y):
    return x+y


def test_add_func():
    assert add(1,2) == 3

