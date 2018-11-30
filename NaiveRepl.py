from .mechanics.Repl import replacer
from time import time


def trans_long_ngrams(word):
    long_ngram_dict = {'sch':'ш', 'ya':'я', '\Aand\Z':'энд'}
    new_word = replacer(word, long_ngram_dict)
    return new_word


def trans_ends(word):
    ends_ngrams_dict = {'\Ay(?=[euioa])':'й',
                        '\Ae(?![euioay-])':'э',
                        '(?<=[euioa])y\Z':'й',
                        '(?<![euioa])y\Z':'и'}
    new_word = replacer(word, ends_ngrams_dict)
    return new_word


def trans_short_ngrams(word):
    short_ngrams_dict = {'qu':'кв', 'ch':'ч', 'sh':'ш', 'ck':'к', 'th':'т',
                         'ph':'ф', 'sc':'ск', 'you':'ю'}
    new_word = replacer(word, short_ngrams_dict)
    return new_word


def trans_literals(word):
    ngrams_dict = {'b':'б', 'c':'c', 'd':'д', 'f':'ф', 'g':'г', 'h':'х',
                   'j':'й', 'k':'к', 'l':'л', 'm':'м', 'n':'н', 'p':'п',
                   'q':'к', 'r':'р', 's':'с', 't':'т', 'v':'в', 'w':'в',
                   'x':'х', 'z':'з', 'a+':'а',  'e+':'е',  'i+':'и',
                   'u+':'у', 'o+':'о',  'y+':'и',
                   'ß':'сс', 'ö':'о', 'ä':'а', 'ü':'у', 'é':'е', 'è':'е',
                   'à':'а', 'ù':'у', 'ê':'е', 'â':'а', 'ô':'о', 'î':'и',
                   'û':'у', 'ë':'е', 'ï':'и', 'ÿ':'и', 'ç':'с'}
    new_word = replacer(word, ngrams_dict)
    return new_word


def process(word):
    start_time = time()
    long_ngrams_replaced = trans_long_ngrams(word.replace("'", ''))
    ends_replaced = trans_ends(long_ngrams_replaced)
    short_ngrams_replaced = trans_short_ngrams(ends_replaced)
    simple_ngrams_replaced = trans_literals(short_ngrams_replaced)
    duration = time() - start_time
    return simple_ngrams_replaced, duration

