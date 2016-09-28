# Going to test binsearch
print("testing")
from pytest import raises
from binsearch import binary_search

def test_empty_list():
    assert binary_search([],6) == -1

def test_muliple_instances():
    assert binary_search([0,3,3,4,5,9],3) in [1,2]

def test_nan_in_list():
    assert binary_search([1,float('NaN'),3,5,float('NaN')],2) == 1

def test_inf_in_list():
    assert binary_search([2,float('Inf'),5,7,9],5)==2
# py.test --doctest-modules --cov --cov-report term-missing binsearch.py test_binsearch.py
