from Replacer import replacer


def trans_long_ngrams(word):
    long_ngrams_dict = {'\Athe':'зе', 'thi':'зи', 'out':'аут',
                        'ture':'чур', 'down':'даун', 'super':'супер',
                        'chicago':'чикаго', 'rea':'реа',
                        'tion':'шен', 'ssion':'шн', 'tient':'шент',
                        'ire\Z':'ая', 'ay':'ей', 'ir':'ер',
                        'your':'ер', 'you':'ю', 'all':'ол', 'who':'ху',
                        'zoo':'зоо', '\Aeng':'инг', 'ea':'и'}
    new_word = replacer(word, long_ngrams_dict)
    return new_word


def trans_conditional(word):
    condit_ngrams_dict = {'(?<=[euioay])s(?=[euioay])':'з',
                          # consonants + vowels
                          'c(?=[eiy])':'с', 'g(?=[eiy])':'дж',
                          'a(?=[uw])':'о',
                          # combinaions: war, wr(eiouay)
                          '(?<=w)a(?=r)':'о',
                          '\Awr(?=\w[euioay])':'р',
                          # letters + futher combinations
                          'ea(?=(d|th|lth|sure|sant))':'е',
                          #'i(?=(ld|nd|gn|gh))':'ай',
                          't(?=(ure|ural|ury))':'ч',
                          # beginning of the word
                          '\Ae(?![euioay-])':'э',
                          '\Au(?![euioay-])':'ю',
                          '\Ath':'с', '\Aye':'е',
                          '\Aa':'а', '\Ao':'о', '\Aeu':'ев',
                          # end of the word
                          'ie\Z':'ай', 'ies\Z':'ис',
                          'th\Z':'с', 'ey\Z':'и', 'ow':'оу',
                          # open syllable
                          '(?<=[^euioay])u(?=\w[euioay])':'ью',
                          '(?<=[^euioay])a(?=\w[euioay])':'ей',
                          # closed syllable
                          '(?<=[^euioay])u(?=[^euioay]{2})':'а',
                          '(?<=[^euioay])u(?=[^euioay]\Z)':'а',
                          # empty letters
                          'e\Z':'', 'gh\Z':''}
    new_word = replacer(word, condit_ngrams_dict)
    return new_word


def trans_short_ngrams(word):
    short_ngrams_dict = {'ie':'и',
                         'ue':'ью', 'eu':'ью', 'ew':'ью',
                         'al':'ол', 'ck':'к', 'ch':'ч',
                          'eo':'и', 'ee':'и',
                         'or':'ор', 'oar':'ор', 'oo':'у',
                         'ya':'я', 'ye':'е', 'yu':'ю',
                         'qu':'кв', 'sh':'ш', 'ph':'ф', 'th':'з'}
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
    long_ngrams_replaced = trans_long_ngrams(word)
    condit_ngrams_replaced = trans_conditional(long_ngrams_replaced)
    short_ngrams_replaced = trans_short_ngrams(condit_ngrams_replaced)
    literals_replaced = trans_literals(short_ngrams_replaced)
    return literals_replaced

