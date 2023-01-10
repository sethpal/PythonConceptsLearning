import math

import pytest


@pytest.fixture()
def input_value():
    input =39
    return input
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.parametrize("a,b",[(1,2),(2,2)])
def test_sqr(a,b):
    assert math.pow(a, b) == a * b

def test_Equality():
    assert 10 == 11
@pytest.mark.parametrize("input",[(input_value)])
def test_fixtures(input):
    assert input / 3 == 0