from Replacer import replacer
from time import time


def punc(word):
    punc_dict = {"'(?=[^euioay])":""}
    new_word = replacer(word, punc_dict)
    return new_word


def trans_long_ngrams(word):
    long_ngram_dict = {"sch":"ш", "eau\Z":"о", "your":"ер", "ya":"я"}
    new_word = replacer(word, long_ngram_dict)
    return new_word


def trans_ends(word):
    ends_ngrams_dict = {"\Ay(?=[euioa])":"й",
                        "\Ae(?=[^euioay-])":"э",
                        "(?<=[euioa])y\Z":"й",
                        "(?<=[^euioa])y\Z":"и",
                        "z\Z":"ц", "ea\Z":"и"}
    new_word = replacer(word, ends_ngrams_dict)
    return new_word


def trans_short_ngrams(word):
    short_ngrams_dict = {"qu":"кв", "ch":"ч", "sh":"ш", "ck":"к", "th":"т",
                         "ee":"и", "ue":"ью", "oo":"у", "xx":"хх", "yu":"ю",
                         "ey":"ей", "ph":"ф", "ts":"ц", "you":"ю"}
    new_word = replacer(word, short_ngrams_dict)
    return new_word


def trans_literals(word):
    ngrams_dict = {"b":"б", "c":"к", "d":"д", "f":"ф", "g":"г", "h":"х",
                   "j":"дж", "k":"к", "l":"л", "m":"м", "n":"н", "p":"п",
                   "q":"к", "r":"р", "s":"с", "t":"т", "v":"в", "w":"в",
                   "x":"кс", "z":"з", "a":"а",  "e":"е",  "i":"и",  "u":"у",
                   "o":"о",  "y":"и"}
    new_word = replacer(word, ngrams_dict)
    return new_word


def process(word):
    start_time = time()
    unpuncted_word = punc(word)
    long_ngrams_replaced = trans_long_ngrams(unpuncted_word)
    ends_replaced = trans_ends(long_ngrams_replaced)
    short_ngrams_replaced = trans_short_ngrams(ends_replaced)
    simple_ngrams_replaced = trans_literals(short_ngrams_replaced)
    duration = time() - start_time
    return simple_ngrams_replaced, duration

