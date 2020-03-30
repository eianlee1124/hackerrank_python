#!/usr/bin/env python3

from itertools import combinations

N = int(input())
S = input().split(' ')
K = int(input())


count = 0
contain = 0

for combination in combinations(S, K):
    count += 1
    contain += "a" in combination
    
print(contain / count)