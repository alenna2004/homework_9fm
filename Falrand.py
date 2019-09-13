from sum import get_sum
from random import randint
def test_rand_sum():
    for i in range(1000):
        a = randint(-100,100)
        b = randint(-100,100)
        assert(get_sum(a,b) == a - b)