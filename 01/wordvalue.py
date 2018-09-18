from data import DICTIONARY, LETTER_SCORES
import unittest


def load_words():
    """Load dictionary into a list and return list"""
    word_list = [line.rstrip("\n") for line in open(DICTIONARY)]
    return word_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[letter] for letter in word.upper() if letter in LETTER_SCORES.keys()])


def max_word_value(list_words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    max_word = ""
    for word in list_words:
        if calc_word_value(word) > max_value:
            max_value = calc_word_value(word)
            max_word = word
    return max_word


max_word_value()

if __name__ == "__main__":
    import test_wordvalue
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromModule(test_wordvalue))
    unittest.TextTestRunner().run(suite)
