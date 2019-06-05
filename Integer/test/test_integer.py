import Integer.integr as integr
import pytest
def test_basic():
    '''
    >>> integr.parse('1,3,5,9')
    [1, 3, 5, 9]
    '''

    test_list=integr.parse('1,3,5,9')
    target_list=[1,3,5,9]
    assert test_list==target_list

def test_bad1():
    with pytest.raises(ValueError):
        integr.parse('bad input')

@pytest.mark.xfail(raises=ValueError)
def test_bad2():
    integr.parse('1,3,5,9-1')


@pytest.mark.xfail(raises=ValueError)
def test_bad3():
    '''
    After running this it does not show a failure and shows it as xpassed
    '''
    integr.parse('1,3,5,9')
