from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dict:
        words_list = [word.strip() for word in dict]
    return words_list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES[letter.upper()] for letter in word if letter.isalpha())

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    scores = {word:calc_word_value(word) for word in words}
    return max(scores.keys(), key=lambda k: scores[k])
    
if __name__ == "__main__":
    pass # run unittests to validate