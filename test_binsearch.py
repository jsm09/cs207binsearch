# Going to test binsearch
print("testing")
from pytest import raises
from binsearch import binary_search

def test_empty_list():
    assert binary_search([],6) == -1

def test_muliple_instances():
    assert binary_search([0,3,3,4,5,9],3) in [1,2]

# Tests based on the data types in the array
def test_nan_in_list():
    assert binary_search([1,float('NaN'),3,5,float('NaN')],2) == 1

def test_inf_in_list():
    assert binary_search([2,float('Inf'),5,7,9],5)==2

# Tests based on the placement of the needle in the array
def test_needle_above_range():
    assert binary_search([2,3,6,8,12,34],56) == -1

def test_needle_below_range():
    assert binary_search([5,7,23,46,68,89],2) == -1

def test_needle_last_index():
    assert binary_search([2,3,5,7,23,64],64) == 5

def test_needle_first_index():
    assert binary_search([56,65,71,78],56) == 0
# py.test --doctest-modules --cov --cov-report term-missing binsearch.py test_binsearch.py
