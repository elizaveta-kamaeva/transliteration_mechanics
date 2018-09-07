import re


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

'''
def replacer(word_string, listed_string, literals_dict):
    word_list = word_string.split()
    new_list = [''*len(word_list)]

    for i in range(len(word_list)):
        # replacing the needed ngrams
        word = word_list[i]
        lit_list = listed_string[i]
        for literal in literals_dict:
            # looking for each literal separately
            positions = [match_obj.span()
                         for match_obj in re.finditer(literal, word)]
            if positions:
                for j in range(len(positions)):
                    # starting replacement for each found element
                    start_pos, end_pos = positions[j]
                    if end_pos - start_pos > 1:
                        # if eng ngram is longer than 1 letter
                        for k in range(start_pos+1, end_pos):
                            lit_list[k] = ''
                    lit_list[start_pos] = literals_dict[literal]
            new_word = ''.join(lit_list)
            new_list[i] = new_word
        listed_string[i] = lit_list
    new_string = ' '.join(new_list)
    return new_string, listed_string
'''
