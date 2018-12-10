from collections import OrderedDict
from .mechanics.Repl import replacer


def trans_long_ngrams(word):
    long_ngrams_dict = OrderedDict({
        'cch':'чч', 'zz':'цц', 'lum':'люм'})
    new_word = replacer(word, long_ngrams_dict)
    return new_word


def trans_conditional(word):
    condit_ngrams_dict = OrderedDict({
        '\Az':'з', #old
        '(?<!l)l(?![leuioay-])':'ль', 'l\Z':'ль',
        '(?<![euioay-])z':'ц',
        'cc(?=[ei])':'чч', '(?<!s)c(?=[ei])':'ч',
        'gg?(?=[ei])':'дж',
        '(?<![euioay-])eu(?![euioay-])':'ью',
        '\Ae(?![euioay-])':'э',
        '(?<=[euioa])i(?=\w[euioa])':'й',
        'ue\Z':'ью'})
    new_word = replacer(word, condit_ngrams_dict)
    return new_word


def trans_short_ngrams(word):
    short_ngrams_dict = OrderedDict({
        'cc':'цц', 'ch':'к', 'qu':'кв', 'sh':'ш', 'ts':'ц'})
    new_word = replacer(word, short_ngrams_dict)
    return new_word


def trans_literals(word):
    literal_dict = {
        'b':'б', 'c':'к', 'd':'д', 'f':'ф',
        'g':'г', 'h':'х', 'j':'ж', 'k':'к',
        'l':'л', 'm':'м', 'n':'н', 'p':'п',
        'q':'к', 'r':'р', 's':'с', 't':'т',
        'v':'в', 'w':'в', 'x':'кс', 'z':'з',
        'a+':'а', 'e+':'е', 'i+':'и', 'o+':'о',
        'u+':'у', 'y+':'и'}
    new_word = replacer(word, literal_dict)
    return new_word


def process(word):
    long_ngrams_replaced = trans_long_ngrams(word)
    condit_ngrams_replaced = trans_conditional(long_ngrams_replaced)
    short_ngrams_replaced = trans_short_ngrams(condit_ngrams_replaced)
    literals_replaced = trans_literals(short_ngrams_replaced)
    return literals_replaced
