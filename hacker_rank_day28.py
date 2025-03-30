#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    
    nameList = []
    pattern = '@gmail.com'
    regex = re.compile(pattern)
    
    

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        if regex.search(emailID):
            nameList.append(firstName)
            
    nameList.sort()
    
    for name in nameList:
        print(name)
