import os
from collections import OrderedDict
from .mechanics.Repl import replacer



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
    single_letters_dict = {'\Ab\Z':'би', '\Ac\Z':'си', '\Ad\Z':'ди', '\Af\Z':'эф',
                           '\Ag\Z':'джи', '\Ah\Z':'эйч', '\Aj\Z':'джей', '\Ak\Z':'кей',
                           '\Al\Z':'эль', '\Am\Z':'эм', '\An\Z':'эн', '\Ap\Z':'пи',
                           '\Aq\Z':'кью', '\Ar\Z':'эр', '\As\Z':'эс', '\At\Z':'ти',
                           '\Av\Z':'ви', '\Aw\Z':'дабл ю', '\Ax\Z':'икс', '\Az\Z':'зед',
                           '\Aa\Z':'эй', '\Ao\Z':'оу', '\Ai\Z':'ай', '\Au\Z':'ю',
                           '\Ae\Z':'и', '\Ay\Z':'вай'}
    new_word = replacer(word, single_letters_dict)
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
        # letters + futher combinations
        'ea(?=(d|th|lth|sure|sant))':'е',
        't(?=(ure|ural|ury))':'ч',
        # open syllable
        '(?<=[^euioay])y(?=\w[euioay])':'ай',
        '(?<=[^euioay])a(?=\w[euioay])':'ей',
        # beginning of the word
        '\Ae(?![euioay-])':'э',
        '\Au(?![euioay-])':'ю',
        '\Ath':'с', '\Aeu':'ев',
        '\Ax(?![euioay])':'икс',
        # end of the word
        'ie\Z':'и', 'ies\Z':'ис',
        'th\Z':'с', 'ue\Z':'ю',
        # vowels
        'au':'о',
        # empty letters
        '(?<=[rdgkzb])h(?!\Z)':'',
        '(?=\w{3})e\Z':''})
    new_word = replacer(word, condit_ngrams_dict)
    return new_word


def trans_short_ngrams(word):
    short_ngrams_dict = OrderedDict({'qu':'кв', 'ie':'и', 'ue':'ью', 'eu':'ью',
                         'ck':'к', 'wh':'в', 'ch':'ч', 'th':'з', 'sh':'ш', 'ph':'ф',
                         'ee':'и', 'ey':'и', 'oar':'ор', 'oo':'у',
                         'ya':'я', 'ye':'е', 'yu':'ю', 'yi':'и', 'yo':'йо', 'ea':'и'})
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
	sg_letters_replaced = trans_separate(word)
    words_replaced = trans_words(word)
    long_ngrams_replaced = trans_long_ngrams(words_replaced)
    condit_ngrams_replaced = trans_conditional(long_ngrams_replaced)
    short_ngrams_replaced = trans_short_ngrams(condit_ngrams_replaced)
    literals_replaced = trans_literals(short_ngrams_replaced)
    return literals_replaced

