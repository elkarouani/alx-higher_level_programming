#!/usr/bin/python3

def multiple_returns(sentence):
    return (0, "None") if len(sentence) == 0 else (len(sentence), sentence[0])
