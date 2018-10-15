import re
from string import punctuation


def get_word(line):
    raw_word = line.split(';')[1].strip().lower()
    #raw_word = line.strip().lower()
    word = re.search('[\w&].*[\w&]', raw_word)
    # check if the word is less than 2 characters
    try:
        word = word.group()
    except AttributeError:
        return raw_word, None

    # check if the unpuncted word is less than 2 characters
    word = punc_repl(word)
    if len(word) < 3:
        return raw_word, None

    return raw_word, word


def punc_repl(word_string):
    punc_dict = {}
    # except '&' because we replace it later
    # except '-' because be leave it tht way
    # except "'" because it helps us detect French
    word_string = re.sub('[dm]r.', 'р ', word_string)
    for letter in re.sub("[&'-]", '', punctuation):
        punc_dict[ord(letter)] = None
    new_string = re.sub('&', ' энд ', word_string.translate(punc_dict))
    return new_string
