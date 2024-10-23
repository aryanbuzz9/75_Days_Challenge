import pytest

def add(x):
    return x+3

def test_method():
    assert add(5)==8