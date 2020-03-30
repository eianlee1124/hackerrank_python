#!/usr/bin/env python3


if __name__ == "__main__":
    lst = []
    N = int(input())

    for i in range(N):
        cmd = input()
        if "print" in cmd:
            print(lst)
        if "insert" in cmd:
            _, index, item = cmd
            lst.insert(index, int(item))
        if "remove" in cmd:
            _, item = args.split(' ')
            lst.remove(int(item))
        if "append" in cmd:
            _, item = args.split(' ')
            lst.append(int(item)
        if "sort" in args:
            lst.sort()
        if "pop" in args:
            lst.pop()
        if "reverse" in args:
            lst.reverse()
