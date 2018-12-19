import re


def replacer(word_string, ngrams_dict):
     word_list = word_string.split()
     # replacing the needed ngrams
     for i in range(len(word_list)):
         for ngram in ngrams_dict:
             word_list[i] = re.sub(ngram, ngrams_dict[ngram], word_list[i])
     new_string = ' '.join(word_list)
     return new_string
