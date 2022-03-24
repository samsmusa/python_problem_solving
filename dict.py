#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    s = sorted(s)
    li = dict()
    for i in s:
        if i not in li:
            li[i]=1
        else:
            li[i] += 1
    aa = dict(sorted(li.items(),key=lambda x : x[1], reverse=True))
    for j,i in enumerate(aa):
        print(i,aa[i])
        if j==2:
            break