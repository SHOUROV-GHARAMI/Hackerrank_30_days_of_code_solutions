#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    sums = []
    for i in range(4):
        for j in range(4):
            total = 0
        for k in range (3):
            for l in range (3):
                if k == 1 and l in [0, 2]:
                    continue
                total += arr[i+k][j+l]
        sums.append(total)
    print(max(sums))
