import re


def get_word(line):
    #old_trans, raw_word = line.split(';')
    listed_string = line.split('\t')
    raw_word = listed_string[1]
    raw_word = raw_word.strip()
    raw_word = raw_word.lower()
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
    new_string = word_string
    literals_dict = {"'":""}
    for literal in literals_dict:
        new_string = re.sub(literal, literals_dict[literal], word_string)
    return new_string



def replacer(word_string, literals_dict):
    word_list = word_string.split()

    # replacing the needed ngrams
    for i in range(len(word_list)):
        word = word_list[i]
        for literal in literals_dict:
            word = re.sub(literal, literals_dict[literal], word)
            word_list[i] = word
    new_string = ' '.join(word_list)
    return new_string
