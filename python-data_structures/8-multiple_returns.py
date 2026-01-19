#!/usr/bin/python3


def multiple_returns(sentence):
    long = len(sentence)
    if long == 0:
        char_1 = None
    else:
        char_1 = sentence[0]

    return (long, char_1)
