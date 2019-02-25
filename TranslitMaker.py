'''
from .mechanics.Getter import get_word
from . import NaiveRepl
from . import LanguageDetector
from . import SpecRepl
'''
import re

from language_modules import NaiveRepl
from mechanics import SpecRepl, LanguageDetector


def translit(word):
    # naive translit
    naive_trans = NaiveRepl.process(word)

    # defining the language
    language = LanguageDetector.process(word)

    # translit in a specific language
    spec_trans = SpecRepl.delegator(language, word)

    if naive_trans != spec_trans:
        return [spec_trans, naive_trans]
    else:
        return [spec_trans]


existing_words = set()
def trans_full_string(word):
    global existing_words

    # if the line is inappropriate, take another line
    if not word or word in existing_words:
        return None

    transes = []
    # naive translit
    naive_trans = NaiveRepl.process(word)

    # defining the language
    language = LanguageDetector.process(word)

    # translit in a specific language
    spec_trans = SpecRepl.delegator(language, word)

    # add translit
    if not naive_trans in existing_words:
        existing_words.add(naive_trans)
        transes.append(naive_trans)

        if spec_trans != naive_trans:
            existing_words.add(spec_trans)
            transes.append(spec_trans)

    return transes


def trans_separate(raw_str, trans_str, existing_words):
    sg_words_dict = {}
    raw_list = re.split('[\s.-]', raw_str)
    trans_list = re.split('[\s.-]', trans_str)
    # if length of a foreign word is equal to length of a cyrillic word
    if len(raw_list) == len(trans_list):
        for i in range(len(raw_list)):
            eng_word = raw_list[i]
            rus_word = trans_list[i]
            # check if we know the cyrillic word and it's length is more than 2
            if len(rus_word) > 2 and rus_word not in existing_words:
                sg_words_dict[rus_word] = eng_word

        return sg_words_dict
