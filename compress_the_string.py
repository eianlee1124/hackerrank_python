#/usr/bin/env python3

from itertools import groupby


strings = input()

groups = []
uniquekeys = []
for k, g in groupby(strings):
    groups.append(len(list(g)))
    uniquekeys.append(int(k))
    
print(*zip(groups, uniquekeys))