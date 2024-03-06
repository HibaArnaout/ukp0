import pytest
from ukp0 import Fibonacci

def test_import():
    # This checks __init__ was set up correctly
    try:
        from ukp0 import Fibonacci
    except ImportError:
        assert False

##### YOUR CODE HERE #####

##########################