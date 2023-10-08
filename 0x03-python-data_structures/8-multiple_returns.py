#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_len = len(sentence)
    first = sentence[:1]
    if sentence == "":
        return (0, None)
    return (sentence_len, first)
