import sys
from prime_number.src.prime import is_prime_number
# Always run from prime/test
sys.path += ['../src'] 

def test_is_prime_1():
    assert is_prime_number(1) == False

def test_is_prime_2():
    assert is_prime_number(2) == True
    
def test_is_prime_3():
    assert is_prime_number(3) == True
    
def test_is_prime_4():
    assert is_prime_number(4) == False
    
def test_is_prime_5():
    assert is_prime_number(5) == True