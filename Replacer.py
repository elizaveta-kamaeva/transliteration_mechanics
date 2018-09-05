import re

def replacer(word_string, literals_dict):
    literals_info = {}
    word_list = word_string.split()
    # finding all the ngrams we're interested in
    for literal in literals_dict:
        literals_info[literal] = word_string.count(literal)
    # replacing the needed ngrams
    for literal in literals_info:
        for i in range(len(word_list)):
            word = word_list[i]
            word = re.sub(literal, literals_dict[literal], word,
                          count=literals_info[literal])
            word_list[i] = word
    new_string = ' '.join(word_list)
    return new_string
