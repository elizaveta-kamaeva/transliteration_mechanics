import re

from language_modules import NaiveRepl
from mechanics import SpecRepl, LanguageDetector


class Brand:
    existing_words = set()

    def __init(self):
        self.word = ''
        self.naive_trans = ''
        self.spec_trans = ''
        self.language = ''
        self.transes = []

        self.raw_list = []
        self.raw_str = ''
        self.trans_str = ''
        self.sg_words_dict = {}

    def trans_full_string(self, word):
        global existing_words

        # if the line is inappropriate, take another line
        if not word or word in existing_words:
            return None

        # naive translit
        self.naive_trans = NaiveRepl.process(word)

        # defining the language
        self.language = LanguageDetector.process(word)

        # translit in a specific language
        self.spec_trans = SpecRepl.delegator(self.language, word)

        # add translit
        if self.naive_trans not in existing_words:
            existing_words.add(self.naive_trans)
            self.transes.append(self.naive_trans)

            if self.spec_trans != self.naive_trans:
                existing_words.add(self.spec_trans)
                self.transes.append(self.spec_trans)
        return self.transes

    def trans_separate(self, raw_str, trans_str):
        self.raw_list = re.split('[\s.-]', raw_str)
        self.trans_list = re.split('[\s.-]', trans_str)
        # if length of foreign word is equal to length of cyrillic word
        if len(self.raw_list) == len(self.trans_list):
            for i in range(len(self.raw_list)):
                eng_word = self.raw_list[i]
                rus_word = self.trans_list[i]
                # check if we know the cyrillic word and it's length is more than 2
                if len(rus_word) > 2 and rus_word not in existing_words:
                    self.sg_words_dict[rus_word] = eng_word

            return self.sg_words_dict
