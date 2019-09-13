from sum import get_sum
from random import choice
al = "abcdefghigklmnopqrstuvwxyz"
def test_rand_sum():
    for i in range(1000):
        a = choice(al)
        b = choice(al)
        assert(get_sum(a,b) == a + b)