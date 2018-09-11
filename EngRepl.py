from Mechanics import replacer


def trans_words(word):
    eng_file = open('texts/eng_trans.txt', 'r', encoding='utf-8')
    words_dict = {}
    for line in eng_file:
        eng_word, ru_word = line.split(':')
        words_dict[eng_word] = ru_word.strip()
    new_word = replacer(word, words_dict)
    return new_word

def trans_long_ngrams(word):
    long_ngrams_dict = {'ay':'ей', 'ir':'ер', '\wur':'ер',
                        'you':'ю', 'ea':'и', 'au':'о'}
    new_word = replacer(word, long_ngrams_dict)
    return new_word


def trans_conditional(word):
    condit_ngrams_dict = {'(?<=[euioay])s(?=[euioay])':'з',
                          # consonants + vowels
                          'c(?=[eiy])':'с', '(?<!g)g(?=[eiy])':'дж',
                          'a(?=[uw])':'о',
                          # combinaions of particular letters
                          '(?<=w)a(?=r)':'о',
                          '\Awr(?=\w[euioay])':'р',
                          # letters + futher combinations
                          'ea(?=(d|th|lth|sure|sant))':'е',
                          #'i(?=(ld|nd|gn|gh))':'ай',
                          't(?=(ure|ural|ury))':'ч',
                          # open syllable
                          '(?<=[^euioay])u(?=\w[euioay])':'ю',
                          '(?<=[^euioay])a(?=\w[euioay])':'ей',
                          # closed syllable
                          '(?<=[^euioay])u(?=[^euioay]{2})':'а',
                          '(?<=[^euioay])u(?=[^euioay]\Z)':'а',
                          # beginning of the word
                          '\Ae(?![euioay-])':'э',
                          '\Au(?![euioay-])':'ю',
                          '\Ath':'с', '\Aye':'е', '\Ay':'й',
                          '\Aa':'а', '\Ao':'о', '\Aeu':'ев',
                          # end of the word
                          'ie\Z':'ай', 'ies\Z':'ис',
                          'th\Z':'с', 'ow':'оу',
                          # empty letters
                          '(?<=[^euioay-])h(?!\Z)':'',
                          'e\Z':'', 'gh\Z':''}
    new_word = replacer(word, condit_ngrams_dict)
    return new_word


def trans_short_ngrams(word):
    short_ngrams_dict = {'qu':'кв', 'ie':'и', 'ue':'ью', 'eu':'ью',
                         'ew':'ью', 'ck':'к',
                         'ch':'ч', 'th':'з',
                         'sh':'ш', 'ph':'ф',
                         'eo':'и', 'ee':'и', 'ey':'и',
                         'oar':'ор', 'oo':'у',
                         'ya':'я', 'ye':'е', 'yu':'ю'}
    new_word = replacer(word, short_ngrams_dict)
    return new_word


def trans_literals(word):
    literal_dict = {'b':'б', 'c':'к', 'd':'д', 'f':'ф', 'g':'г',
                    'h':'х', 'k':'к', 'l':'л', 'm':'м', 'n':'н',
                    'p':'п', 'q':'к', 'r':'р', 's':'с', 't':'т',
                    'v':'в', 'w':'в', 'x':'кс', 'z':'з', 'a':'а',
                    'e':'е', 'i':'и', 'o':'о', 'u':'у', 'y':'и', 'j':'дж'}
    new_word = replacer(word, literal_dict)
    return new_word


def process(word):
    words_replaced = trans_words(word)
    long_ngrams_replaced = trans_long_ngrams(words_replaced)
    condit_ngrams_replaced = trans_conditional(long_ngrams_replaced)
    short_ngrams_replaced = trans_short_ngrams(condit_ngrams_replaced)
    literals_replaced = trans_literals(short_ngrams_replaced)
    return literals_replaced

