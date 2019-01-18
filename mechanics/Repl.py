import re


def replacer(word_string, ngrams_dict):
     word_list = word_string.split()
     # replacing the needed ngrams
     for i in range(len(word_list)):
         for ngram in ngrams_dict:
             word_list[i] = re.sub(ngram, ngrams_dict[ngram], word_list[i])
     new_string = ' '.join(word_list)
     return new_string


def replace_abbreviations(word_string, ngrams_dict):
    word_list = word_string.split()
    for i in range(len(word_list)):
        # checking single letters in a word
        sg_letter_found = re.search('(\\s|^|-|\.)\w(\\s|$|-|\.)', word_list[i])

        # checking words consisting of consonants only
        consonants_word_found = re.fullmatch('[^euioayыаеэяиюу]+', word_list[i])
        if sg_letter_found or consonants_word_found:
            # if any found, replacing it and adding spaces on the both sides of a letter
            for ngram in ngrams_dict:
                word_list[i] = re.sub(ngram, ' {} '.format(ngrams_dict[ngram]), word_list[i])
    new_string = ' '.join(word_list)
    return new_string
