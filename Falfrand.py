from sum import get_sum
from random import uniform
def test_rand_sum():
    for i in range(1000):
        a = uniform(-100,100)
        b = uniform(-100,100)
        assert(get_sum(a,b) == a - b)