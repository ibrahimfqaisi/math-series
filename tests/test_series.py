import pytest
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series



def test_fibonacci_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected  
def test_fibonacci_Tow():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected  
def test_fibonacci_three():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected  
def test_fibonacci_four():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected  
def test_fibonacci_five():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected  
    
def test_fibonacci_six():
    actual = fibonacci("hi")
    expected = "please add number"
    assert actual == expected  
    

def test_lucas_one():
    actual = lucas(0)
    expected = 2
    assert actual == expected  
def test_lucas_Tow():
    actual = lucas(1)
    expected = 1
    assert actual == expected  
def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected  
def test_lucasi_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected  
def test_lucas_five():
    actual = lucas(10)
    expected = 123
    assert actual == expected  
    
def test_lucas_six():
    actual = lucas("hi")
    expected = "please add number"
    assert actual == expected  
    
    
    
def test_sum_series_one():
    actual = sum_series(0)
    expected = 0
    assert actual == expected  
def test_sum_series_two():
    actual = sum_series(1)
    expected = 1
    assert actual == expected  
def test_sum_series_three():
    actual = sum_series(2)
    expected = 1
    assert actual == expected  
def test_sum_series_four():
    actual = sum_series(3)
    expected = 2
    assert actual == expected  
def test_sum_series_five():
    actual = sum_series(10)
    expected = 55
    assert actual == expected  
    


def test_sum_series_six():
    actual = sum_series(0,2,1)
    expected = 2
    assert actual == expected  
def test_sum_series_seven():
    actual = sum_series(1,2,1)
    expected = 1
    assert actual == expected  
def test_sum_series_eight():
    actual = sum_series(3,2,1)
    expected = 4
    assert actual == expected  
def test_sum_series_nine():
    actual = sum_series(4,2,1)
    expected = 7
    assert actual == expected  
def test_sum_series_ten():
    actual = sum_series(10,2,1)
    expected = 123
    assert actual == expected  
    
    
def test_sum_series_eleven():
    actual = sum_series(0,2,2)
    expected = 2
    assert actual == expected  
def test_sum_series_twelve():
    actual = sum_series(1,2,2)
    expected = 2
    assert actual == expected  
def test_sum_series_thirteen():
    actual = sum_series(3,2,2)
    expected = 6
    assert actual == expected  
def test_sum_series_fourteen():
    actual = sum_series(4,2,4)
    expected = 16
    assert actual == expected  
def test_sum_series_fifteen():
    actual = sum_series(3,5,3)
    expected = 11
    assert actual == expected  
    
    
def test_lucas_sixteen():
    actual = lucas("hi")
    expected = "please add number"
    assert actual == expected  