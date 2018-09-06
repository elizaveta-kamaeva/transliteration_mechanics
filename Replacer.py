import re

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
