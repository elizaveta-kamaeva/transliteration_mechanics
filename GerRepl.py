from collections import OrderedDict
#from .mechanics.Repl import replacer
from mechanics.Repl import replacer


def trans_long_ngrams(word):
    long_ngrams_dict = OrderedDict({
        'tsch':'ч', 'sch':'ш', 'chs':'хс', 'ss':'сс'})
    new_word = replacer(word, long_ngrams_dict)
    return new_word


def trans_conditional(word):
    condit_ngrams_dict = OrderedDict({
        's(?=[euioay])':'з',
        #'\Ah(?=[euioay])':'г',
        '(?<![eiiouay])z(?![euioay])':'ц',
        '(?<=[euoiay])v(?=[euioay])':'в',
        '(?<![euioay])ä':'е',
        '\Ae(?![euioay-])':'э',
        '(?<!\Ai)st':'шт',
        't?z\Z':'ц', '\Ach':'к'})
    new_word = replacer(word, condit_ngrams_dict)
    return new_word


def trans_short_ngrams(word):
    short_ngrams_dict = OrderedDict({
        'ch':'х', 'tz':'ц', 'sp':'шп',
        'ck':'к', 'ph':'ф', 'sh':'ш',
        'eh':'е','je':'е', 'ju':'ю',
        'ja':'я','qu':'кв','ei':'ей',
        'ie':'и', 'eu':'ой'})
    new_word = replacer(word, short_ngrams_dict)
    return new_word


def trans_literals(word):
    literal_dict = {
        'b':'б', 'c':'к', 'd':'д', 'f':'ф',
        'g':'г', 'h':'х', 'j':'й', 'k':'к',
        'l':'л', 'm':'м', 'n':'н', 'p':'п',
        'q':'к', 'r':'р','s':'с', 't':'т',
        'v':'ф', 'w':'в', 'x':'кс', 'z':'з',
        'a':'а', 'e':'е', 'i':'и', 'o':'о',
        'u':'у', 'y':'и', 'ß':'сс', 'ö':'ё',
        'ä':'э', 'ü':'ю'}
    new_word = replacer(word, literal_dict)
    return new_word


def process(word):
    long_ngrams_replaced = trans_long_ngrams(word)
    condit_ngrams_replaced = trans_conditional(long_ngrams_replaced)
    short_ngrams_replaced = trans_short_ngrams(condit_ngrams_replaced)
    literals_replaced = trans_literals(short_ngrams_replaced)
    return literals_replaced
