import os


class Replicator:
    dir = os.path.dirname(os.path.realpath(__file__))
    eng_file = open(os.path.join(dir, 'eng_trans.txt'), 'r', encoding='utf-8')
    eng_repls = eng_file.readlines()
    eng_file.close()

    def __init__(self, word):
        self.word = word
        self.long_ngrams_replaced = {}
        self.short_ngrams_replaced = {}
        self.literals_replaced = {}