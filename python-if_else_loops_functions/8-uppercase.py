#!/usr/bin/python3
def uppercase(str):
    for char in str:
        c = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(c), end="")
    print("{}".format(""))
