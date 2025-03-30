#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
nofSwap = 0
for i in range(0, n-1):
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1],a[i]
            nofSwap +=1
print('Array is sorted in', nofSwap,'swaps.')
print('First Element:',a[0])
print('Last Element:', a[-1])