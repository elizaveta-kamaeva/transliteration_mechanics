import os
from collections import OrderedDict
#from .mechanics.Repl import replacer, replace_abbreviations
from mechanics.Repl import replacer, replace_abbreviations


dir = os.path.dirname(os.path.realpath(__file__))
eng_file = open(os.path.join(dir, 'eng_trans.txt'), 'r', encoding='utf-8')
eng_repls = eng_file.readlines()
eng_file.close()


def trans_words(word):
    words_dict = {}
    for pair in eng_repls:
        eng_word, ru_word = pair.split(':')
        words_dict[eng_word] = ru_word.strip()
    new_word = replacer(word, words_dict)
    return new_word


def trans_separate(word):
    single_letters_dict = {'b':'би', 'c':'си', 'd':'ди', 'f':'эф',
                           'g':'джи', 'h':'эйч', 'j':'джей', 'k':'кей',
                           'l':'эль', 'm':'эм', 'n':'эн', 'p':'пи',
                           'q':'кью', 'r':'эр', 's':'эс', 't':'ти',
                           'v':'ви', 'w':'дабл ю', 'x':'икс', 'z':'зед',
                           'a':'эй', 'o':'оу', 'i':'ай', 'u':'ю',
                           'e':'и', 'y':'вай'}
    new_word = replace_abbreviations(word, single_letters_dict)
    return new_word

def trans_long_ngrams(word):
    long_ngrams_dict = {'ay':'ей','[ao]ught':'от', 'ueu':'е',
                        'you':'ю', 'chr':'кр', 'scq':'ск'}
    new_word = replacer(word, long_ngrams_dict)
    return new_word


def trans_conditional(word):
    condit_ngrams_dict = OrderedDict({
        '(?<=[euioay])s(?=[euioay])':'з',
        'ts(?=\w+)':'ц',
        # consonants + vowels
        'c(?=[eiy])':'с', '(?<!g)g(?=[eiy])':'дж',
        'a(?=[uw])':'о',
        # combinaions of particular letters
        '(?<=w)a(?=r)':'о',
        '\Awr(?=[euioay])':'р',
        'j(?![euioay])':'ж',
        '(?<![euioay])th':'т',
        '(?<!e)ew':'ью',
        'ow(?=\w{2})': 'оу',
        'l(?=t)':'ль',
        # letters + futher combinations
        'ea(?=(d|th|lth|sure|sant))':'е',
        't(?=(ure|ural|ury))':'ч',
        # open syllable
        '(?<=[^euioay])y(?=\w[euioay])':'ай',
        '(?<=[^euioay])a(?=\w[euioay])':'ей',
        '(?<=[^euioay])i(?=\we\Z)': 'ай',
        # beginning of the word
        '\Ae(?![euioay-])':'э',
        '\Au(?![euioay-])':'ю',
        '\Ath':'с', '\Aeu':'ев',
        '\Ax(?![euioay])':'икс',
        # end of the word
        'ie\Z':'и', 'ies\Z':'ис',
        'th\Z':'с', 'ue\Z':'ю',
        'ey\Z': 'и', 'ai\Z': 'ай',
        # vowels
        'au':'о',
        '[ae]i|ey':'ей',
        # empty letters
        '(?<=[rdgkzb])h(?!\Z)':'',
        '(?<=\w{3})e\Z':''})
    new_word = replacer(word, condit_ngrams_dict)
    return new_word


def trans_short_ngrams(word):
    short_ngrams_dict = OrderedDict({'qu':'кв', 'ie':'и', 'ue':'ью', 'eu':'ью',
                         'ck':'к', 'wh':'в', 'ch':'ч', 'th':'з', 'sh':'ш', 'ph':'ф',
                         'ee':'и', 'oar':'ор', 'oo':'у',
                         'ya':'я', 'ye':'е', 'yu':'ю', 'yi':'и', '\Ayo':'йо', 'ea':'и'})
    new_word = replacer(word, short_ngrams_dict)
    return new_word


def trans_literals(word):
    literal_dict = {'b':'б', 'c':'к', 'd':'д', 'f':'ф', 'g':'г',
                    'h':'х', 'k':'к', 'l':'л', 'm':'м', 'n':'н',
                    'p':'п', 'q':'к', 'r':'р', 's':'с', 't':'т',
                    'v':'в', 'w':'в', 'x':'кс', 'z':'з', 'a':'а',
                    'e':'е', 'i+':'и', 'o':'о', 'u+':'у', 'y+':'и', 'j':'дж'}
    new_word = replacer(word, literal_dict)
    return new_word


def process(word):
    words_replaced = trans_words(word)
    sg_letters_replaced = trans_separate(words_replaced)
    long_ngrams_replaced = trans_long_ngrams(sg_letters_replaced)
    condit_ngrams_replaced = trans_conditional(long_ngrams_replaced)
    short_ngrams_replaced = trans_short_ngrams(condit_ngrams_replaced)
    literals_replaced = trans_literals(short_ngrams_replaced)
    return literals_replaced

