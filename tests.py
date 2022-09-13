import pytest

list123 = [1, 2, 3]

def test_1():
    assert list123[1] == 2

@pytest.mark.parametrize("x,exp", [(0, 1), (2, 3)])
def test_2():
    assert list123[x] == exp

def test_3():
    try:
        assert list123[4] == 1
    except IndexError:
        pass

dict123 = {'a':1, 'b':2, 'c':3}

def test_4():
    assert dict123['a'] == 1

@pytest.mark.parametrize("x,exp", [('b', 2), ('c', 3)])
def test_5():
    assert dict123[x] == exp

def test_6():
    try:
        assert dict123['d'] == 4
    except KeyError:
        pass

    
