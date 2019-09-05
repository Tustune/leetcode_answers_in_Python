# Hamming Distance 汉明距离

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'

import sys
sys.path.append('.')
from schema import time_it


class Solution(object):
    @classmethod
    @time_it
    def hammingDistance(self, x, y):
        a = x ^ y
        count = 0

        while a != 0:
            count += 1
            a &= a-1
        return count


case1 = (1, 4)
assert Solution.hammingDistance(*case1) == 2
