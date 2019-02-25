import re


class Repler:
    def replacer(self, word_string, ngrams_dict):
        self.word_string = word_string
        self.ngram_dict = ngrams_dict
        word_list = word_string.split()

        # replacing the needed ngrams
        for i in range(len(word_list)):
         for ngram in ngrams_dict:
             word_list[i] = re.sub(ngram, ngrams_dict[ngram], word_list[i])

        self.new_string = ' '.join(word_list)


    def replace_abbreviations(self, word_string, ngrams_dict):
        self.word_string = word_string
        self.word_list = word_string.split()
        for i in range(len(self.word_list)):
            # checking single letters in a word
            self.sg_letter_found = re.search('(\\s|^|-|\.)\w(\\s|$|-|\.)', self.word_list[i])

            # checking words consisting of consonants only
            self.consonants_word_found = re.fullmatch('[^euioayыаеэяиюу]+', self.word_list[i])
            if self.sg_letter_found or self.consonants_word_found:

                # if any found, replacing it and adding spaces on the both sides of a letter
                for ngram in ngrams_dict:
                    self.word_list[i] = re.sub(ngram, ' {} '.format(ngrams_dict[ngram]), self.word_list[i])

        self.new_string = ' '.join(self.word_list)
