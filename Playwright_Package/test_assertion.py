# demo 1

def test_demo_pytest():
    assert 1+1 == 2

# demo 2 of multiple assertions

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0



# demo- preferred method for multiple assertions

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_zeroes():
    assert add(0, 0) == 0

def test_add_negative_and_positive():
    assert add(-1, 1) == 0