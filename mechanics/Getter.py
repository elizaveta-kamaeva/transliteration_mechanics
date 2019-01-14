import re
from string import punctuation


def get_word(line):
    #raw_word = line.strip().lower()
    raw_word = line.split(';')[1].strip().lower()
    #raw_word = line.split(';')[0].strip().lower()
    # getting word no shorter than 2 characters
    word = re.search('[\w&].*[\w&]', raw_word)
    if word:
        word = word.group()
    else:
        return raw_word, None

    # check if the unpuncted word is equal or less than 2 characters
    word = punc_repl(word)
    if len(word) < 3:
        return raw_word, None
    else:
        return raw_word, word


def punc_repl(word_string):
    punc_dict = {}
    # except '&' because we replace it later
    # except '-' because be leave it that way
    # except "'" because it helps us to detect French
    # dot at "dr." & "mr." we replace with a space
    word_string = re.sub('(?<=[dm]r)\.', ' ', word_string)
    for letter in re.sub("[&'-]", '', punctuation):
        punc_dict[ord(letter)] = None
    new_string = re.sub('&', ' энд ', word_string.translate(punc_dict))
    return new_string
