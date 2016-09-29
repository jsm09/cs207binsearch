from pytest import raises
from binsearch import binary_search
print("testing")
# Tests based on the length of the array
def test_empty_list():
    print('it ran!!!')
    assert binary_search([],6) == -1
def test_one_element_list():
    assert binary_search(['s'],'s') == 0
def test_two_element_list():
    assert binary_search([float(3.45),4],3.45) == 0

# Tests based on number of times needle appears in the array
def test_two_instances():
    assert binary_search([0,3,3,4,5,9],3) in [1,2]
def test_three_instances():
    assert binary_search([float(3.4),5,7,10,15,15,15], 15) in [4,5,6]
def test_no_instances():
    assert binary_search(['a','b','c','e','f'],'d') == -1

# Tests based on the data types in the array
def test_nan_in_list():
    assert binary_search([1,float('NaN'),3,5,float('NaN')],2) == 1
def test_inf_in_list():
    assert binary_search([2,float('Inf'),5,7,9],5) == 2
def test_floats_and_ints():
    assert binary_search([2,3.5,6,float64(34),float(56),float(87),98],34) == 3
def test_strings():
    assert binary_search(['alice','ben','ceyon','david','esther'],'ben') == 1

# Tests based on the placement of the needle in the array
def test_needle_above_range():
    assert binary_search([2,3,6,8,12,34],56) == -1
def test_needle_below_range():
    assert binary_search([5.3,7.4,23,46.2323,68.54,89],2) == -1
def test_needle_last_index():
    assert binary_search([2,3,5,7,23,64],64) == 5
def test_needle_first_index():
    assert binary_search([56,65,71,78],56) == 0

# Tests based on incompatibility of the needle and the array
def test_needle_float_array_int():
    assert binary_search([1,2,3,4,5],float(3)) == 2
def test_needle_int_array_float():
    assert binary_search([1.0,2.0,3.0,4,5],3) == 2
def test_string_upper_lower():
    assert binary_search(['a','b','c'],'A') == 1

# py.test --doctest-modules --cov --cov-report term-missing binsearch.py test_binsearch.py
