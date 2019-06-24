from main import *

def test_add():
    assert add(1, 2) == 3

def test_substract():
    assert substract(2, 1) == 1

def test_increment():
    assert increment(1) == 2

def test_decrement():
    assert decrement(2) == 1
