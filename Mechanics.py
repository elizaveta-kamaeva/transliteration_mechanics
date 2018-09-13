import re
from string import punctuation


def get_word(line):
    raw_word = line.split(';')[1].strip().lower()
    word = re.search('[\w&].*[\w&]', raw_word)
    try:
        word = word.group()
    except:
        print('The string "{}" is empty '
            'or less than 2 characters.'.format(raw_word))
        return raw_word, None

    word = punc_repl(word)
    if len(word) < 3:
        print('The word "{}" is too short to analyze'.format(raw_word))
        return raw_word, None

    return raw_word, word


def punc_repl(word_string):
    punc_dict = {}
    for letter in punctuation.replace('-', ''):
        punc_dict[ord(letter)] = None
    new_string = word_string.translate(punc_dict)
    return new_string


def replacer(word_string, literals_dict):
    word_list = word_string.split()
    # replacing the needed ngrams
    for i in range(len(word_list)):
        for literal in literals_dict:
            word_list[i] = re.sub(literal, literals_dict[literal], word_list[i])
    new_string = ' '.join(word_list)
    return new_string
