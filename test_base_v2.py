from base_file import (
    a, 
    b,
    add, 
    subtract,
    multiply,
    divide
)


print(a, b, add(a, b), subtract(a, b), multiply(a, b), divide(a, b))

def test_mul():

    assert multiply(5, 10) == 50

def test_divide():
    assert divide(10, 5) == 2

