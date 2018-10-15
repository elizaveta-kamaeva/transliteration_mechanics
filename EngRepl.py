from collections import OrderedDict
from mechanics.Repl import replacer


def trans_words(word, eng_file):
    words_dict = {}
    eng_file.seek(0)
    for line in eng_file:
        eng_word, ru_word = line.split(':')
        words_dict[eng_word] = ru_word.strip()
    new_word = replacer(word, words_dict)
    return new_word


def trans_long_ngrams(word):
    long_ngrams_dict = {'ay':'ей', 'au':'о',
                        'you':'ю', 'chr':'кр'}
    new_word = replacer(word, long_ngrams_dict)
    return new_word


def trans_conditional(word):
    condit_ngrams_dict = OrderedDict({
        '(?<=[euioay])s(?=[euioay])':'з',
        # consonants + vowels
        'c(?=[eiy])':'с', '(?<!g)g(?=[eiy])':'дж',
        'a(?=[uw])':'о',
        # combinaions of particular letters
        '(?<=w)a(?=r)':'о',
        '\Awr(?=\w[euioay])':'р',
        'j(?![euioay])':'ж',
        '(?![euioay])th':'т',
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
        # empty letters
        '(?<=[dgkzb])h(?!\Z)':'',
        'e\Z':'', 'gh\Z':''})
    new_word = replacer(word, condit_ngrams_dict)
    return new_word


def trans_short_ngrams(word):
    short_ngrams_dict = OrderedDict({'qu':'кв', 'ie':'и', 'ue':'ью', 'eu':'ью',
                         '[^e]ew':'ью', 'ck':'к', 'ts':'ц', 'wh':'в',
                         'ch':'ч', 'th':'з', 'sh':'ш', 'ph':'ф',
                         'ee':'и', 'ey':'и',
                         'oar':'ор', 'oo':'у',
                         'ya':'я', 'ye':'е', 'yu':'ю', 'yi':'и',
                         'ea':'и'})
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


def process(word, eng_file):
    words_replaced = trans_words(word, eng_file)
    long_ngrams_replaced = trans_long_ngrams(words_replaced)
    condit_ngrams_replaced = trans_conditional(long_ngrams_replaced)
    short_ngrams_replaced = trans_short_ngrams(condit_ngrams_replaced)
    literals_replaced = trans_literals(short_ngrams_replaced)
    return literals_replaced

