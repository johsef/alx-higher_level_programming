#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with the
    lenght of the string as first character
    """
    if len(sentence) == 0:
        sentence = ("None",)
        return((len(sentence) - 1, sentence[0]))
    return((len(sentence), sentence[0]))
