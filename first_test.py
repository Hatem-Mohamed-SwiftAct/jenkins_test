#------------------------------- Import Libraries -------------------------------#
# Import the PyTest Library
from library import *

# Import time module to add delays (if needed)
import time

#----------------------------- Sequence 1 -------------------------------#
def test_sum():
    x = 1
    y = 2

    result = sum(x,y)
    assert result == 3, "It Failed"
