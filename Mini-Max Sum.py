#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum1 =0
    sum2= 0
    sum1 =sum(arr)-min(arr)
    sum2 =sum(arr)-max(arr)
    print(sum2,sum1)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
