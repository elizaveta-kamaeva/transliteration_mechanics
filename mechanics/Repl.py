import re


def replacer(word_string, literals_dict):
     word_list = word_string.split()
     # replacing the needed ngrams
     for i in range(len(word_list)):
         for literal in literals_dict:
             word_list[i] = re.sub(literal, literals_dict[literal], word_list[i])
     new_string = ' '.join(word_list)
     return new_string
