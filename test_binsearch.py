# Going to test binsearch
print("testing")
from pytest import raises
from binsearch import binary_search

def test_empty_list():
    assert binary_search([]) == -1

def test_muliple_instances():
    assert binary_search([0,3,3,4,5,9],3) in [1,2]

def test_nan_in_list():
    assert binary_search([float('NaN'),3,5,float(NaN)],3) == 45

def test_inf_in_list():
    assert binary_search([2,float('Inf'),5,7,9],)
