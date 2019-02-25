import os
from collections import OrderedDict
from language_modules.repl import Replicator
from mechanics.Repl import replacer, replace_abbreviations


class EngReplicator(Replicator):

    single_letters_dict = {'b': 'би', 'c': 'си', 'd': 'ди', 'f': 'эф',
                           'g': 'джи', 'h': 'эйч', 'j': 'джей', 'k': 'кей',
                           'l': 'эль', 'm': 'эм', 'n': 'эн', 'p': 'пи',
                           'q': 'кью', 'r': 'эр', 's': 'эс', 't': 'ти',
                           'v': 'ви', 'w': 'дабл ю', 'x': 'икс', 'z': 'зед',
                           'a': 'эй', 'o': 'оу', 'i': 'ай', 'u': 'ю',
                           'e': 'и', 'y': 'вай'}
    long_ngrams_dict = {'ay': 'ей', '[ao]ught': 'от', 'ueu': 'е',
                        'you': 'ю', 'chr': 'кр', 'scq': 'ск'}

    condit_ngrams_dict = OrderedDict({
            '(?<=[euioay])s(?=[euioay])': 'з',
            'ts(?=\w+)': 'ц',
            # consonants + vowels
            'c(?=[eiy])': 'с', '(?<!g)g(?=[eiy])': 'дж',
            'a(?=[uw])': 'о',
            # combinaions of particular letters
            '(?<=w)a(?=r)': 'о',
            '\Awr(?=[euioay])': 'р',
            'j(?![euioay])': 'ж',
            '(?<![euioay])th': 'т',
            '(?<!e)ew': 'ью',
            'ow(?=\w{2})': 'оу',
            'l(?=t)': 'ль',
            # letters + futher combinations
            'ea(?=(d|th|lth|sure|sant))': 'е',
            't(?=(ure|ural|ury))': 'ч',
            # open syllable
            '(?<=[^euioay])y(?=\w[euioay])': 'ай',
            '(?<=[^euioay])a(?=\w[euioay])': 'ей',
            '(?<=[^euioay])i(?=\we\Z)': 'ай',
            # beginning of the word
            '\Ae(?![euioay-])': 'э',
            '\Au(?![euioay-])': 'ю',
            '\Ath': 'с', '\Aeu': 'ев',
            '\Ax(?![euioay])': 'икс',
            # end of the word
            'ie\Z': 'и', 'ies\Z': 'ис',
            'th\Z': 'с', 'ue\Z': 'ю',
            'ey\Z': 'и', 'ai\Z': 'ай',
            # vowels
            'au': 'о',
            '[ae]i|ey': 'ей',
            # empty letters
            '(?<=[rdgkzb])h(?!\Z)': '',
            '(?<=\w{3})e\Z': ''})

    short_ngrams_dict = OrderedDict({'qu': 'кв', 'ie': 'и', 'ue': 'ью', 'eu': 'ью',
                                         'ck': 'к', 'wh': 'в', 'ch': 'ч', 'th': 'з', 'sh': 'ш', 'ph': 'ф',
                                         'ee': 'и', 'oar': 'ор', 'oo': 'у',
                                         'ya': 'я', 'ye': 'е', 'yu': 'ю', 'yi': 'и', '\Ayo': 'йо', 'ea': 'и'})


    literal_dict = {'b': 'б', 'c': 'к', 'd': 'д', 'f': 'ф', 'g': 'г',
                        'h': 'х', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н',
                        'p': 'п', 'q': 'к', 'r': 'р', 's': 'с', 't': 'т',
                        'v': 'в', 'w': 'в', 'x': 'кс', 'z': 'з', 'a': 'а',
                        'e': 'е', 'i+': 'и', 'o': 'о', 'u+': 'у', 'y+': 'и', 'j': 'дж'}

    def __init__(self, word):
        Replicator.__init__(self, word)

        self.word = word
        self.trans_words = replacer(self.word, Replicator.eng_repls)
        self.sg_letters_replaced = replace_abbreviations(self.word, EngReplicator.single_letters_dict)
        self.long_ngrams_replaced = replacer(self.sg_letters_replaced, EngReplicator.long_ngrams_dict)
        self.condit_ngrams_replaced = replacer(self.long_ngrams_replaced, EngReplicator.condit_ngrams_dict)
        self.short_ngrams_replaced = replacer(self.condit_ngrams_replaced, EngReplicator.short_ngrams_dict)
        self.literals_replaced = replacer(self.short_ngrams_replaced, EngReplicator.literal_dict)
