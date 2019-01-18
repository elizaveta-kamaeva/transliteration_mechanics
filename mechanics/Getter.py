import re
from string import punctuation


def get_raw(line):
    # get raw word to show it as a first item os a pair
    raw_word = line.strip().lower()
    # raw_word = line.split(';')[1].strip().lower()
    # raw_word = line.split(';')[0].strip().lower()
    return raw_word


def get_word2process(raw_word):
    # get word no shorter than 2 characters
    word = re.search('[\w&].*[\w&]', raw_word)
    if word:
        word = word.group()
    else:
        return None

    # replace punctuation
    word = punc_repl(word)
    if len(word) < 3:
        return None
    else:
        return word


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
