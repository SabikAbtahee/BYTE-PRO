#!/bin/python3

import sys
def performOperation(a,b,k,list):
    for i in range(a-1,b):
        list[i]+=k



if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]

    list = [0]*n # size will be n
    totalK=[0]*n
    occurence = [0]*5
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]



    print()