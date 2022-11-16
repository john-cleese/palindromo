import re

import unidecode


def check_palindrome(sentence):
    if not sentence:
        return False
    sentence = sentence.lower()
    sentence = sentence.replace(" ", "")
    sentence = unidecode.unidecode(sentence)
    sentence = "".join(re.findall("[a-z]+", sentence))

    if sentence == sentence[::-1]:
        return True
    return False
