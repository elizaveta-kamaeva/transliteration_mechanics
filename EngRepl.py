from collections import OrderedDict
from mechanics.Repl import replacer, repl


def trans_words(word, eng_file):
    words_dict = {}
    eng_file.seek(0)
    for line in eng_file:
        eng_word, ru_word = line.split(':')
        words_dict[eng_word] = ru_word.strip()
    new_word = replacer(word, OrderedDict(words_dict))
    return new_word


def trans_long_ngrams(word):
    long_ngrams_dict = OrderedDict({
        'ay':'ей', 'you':'ю', 'ea':'и', 'au':'о', 'qu':'кв'})
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
        '(?<!l)l(?![leuioay-]|\Z)':'ль',
        # letters + futher combinations
        'ea(?=(d|th|lth|sure|sant))':'е',
        't(?=(ure|ural|ury))':'ч',
        # open syllable
        '(?<=[^euioay])u(?=\w[euioay])':'ю',
        '(?<=[^euioay])u(?=[euioay])':'ю',
        '(?<=[^euioay])a(?=\w[euioay])':'ей',
        '(?<=[^euioay])y(?=\w[euioay])':'ай',
        # closed syllable
        '(?<=[^euioay])u(?![euioay]{2})':'а',
        # beginning of the word
        '\Ae(?![euioay-])':'э',
        '\Au(?![euioay-])':'ю',
        '\Ath':'с', '\Aye':'е', '\Ay':'й',
        '\Aeu':'ев',
        # end of the word
        '(?<=[euioay])y':'й',
        'ie\Z':'и', 'ies\Z':'ис',
        'th\Z':'с', 'ue\Z':'ю',
        # empty letters
        '(?<=[rdgkzb])h(?!\Z)':'',
        'e\Z':'', 'gh\Z':''})
    new_word = replacer(word, condit_ngrams_dict)
    return new_word


def trans_short_ngrams(word):
    short_ngrams_dict = OrderedDict({
        'ie':'и', 'ue':'ью', 'eu':'ью',
        'ew':'ью', 'ow':'оу', 'ck':'к', 'ts':'ц',
        'ch':'ч', 'th':'з', 'sh':'ш', 'ph':'ф',
        'eo':'и', 'ee':'и', 'ey':'и', 'ai':'ей',
        'oar':'ор', 'oo':'у', 'ui':'юи'})
    new_word = replacer(word, short_ngrams_dict)
    return new_word


def trans_literals(word):
    literal_dict = {
        'b':'б', 'c':'к', 'd':'д', 'f':'ф', 'g':'г',
        'h':'х', 'k':'к', 'l':'л', 'm':'м', 'n':'н',
        'p':'п', 'q':'к', 'r':'р', 's':'с', 't':'т',
        'v':'в', 'w':'в', 'x':'кс', 'z':'з', 'a':'а',
        'e':'е', 'i':'и', 'o':'о', 'u':'у', 'y':'и', 'j':'дж'}
    new_word = replacer(word, literal_dict)
    return new_word


def process(word, eng_file):
    words_replaced = trans_words(word, eng_file)
    long_ngrams_replaced = trans_long_ngrams(word)
    condit_ngrams_replaced = trans_conditional(word)
    short_ngrams_replaced = trans_short_ngrams(word)
    literals_replaced = trans_literals(word)
    final_word = repl(word,
                      words_replaced,
                      long_ngrams_replaced,
                      condit_ngrams_replaced,
                      short_ngrams_replaced,
                      literals_replaced)
    return final_word

