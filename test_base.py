from base_file import (
    a, 
    b,
    add, 
    subtract,
    multiply,
    divide
)


print(a, b, add(a, b), subtract(a, b), multiply(a, b), divide(a, b))

def test_add():

    assert add(5, 10) == 15

def test_subtract():
    assert subtract(10, 5) == 5