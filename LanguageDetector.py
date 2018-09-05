import re


def it_trailer(word):
    it_ngrams = {'zz\w*[euioay]', 'cc\w*[euioay]', ''}
    for ngram in it_ngrams:
        found_ngrams = re.findall(ngram, word)
        if found_ngrams:
            return 1
    return 0


def de_trailer(word):
    de_ngrams = ['haus']
    for ngram in de_ngrams:
        found_ngrams = re.findall(ngram, word)
        if found_ngrams:
            return 1
    return 0


def fr_trailer(word):
    fr_ngrams = ['ouch']
    fr_neg_ngrams = []
    # searching for stop-ngrams
    for neg_ngram in fr_neg_ngrams:
        found_neg_ngrams = re.findall(neg_ngram, word)
        if found_neg_ngrams:
            return 0

    for ngram in fr_ngrams:
        found_ngrams = re.findall(ngram, word)
        if found_ngrams:
            return 1
    return 0


def process(word):
    it_prob = it_trailer(word)
    de_prob = de_trailer(word)
    fr_prob = de_trailer(word)
    prob_dict = {it_prob:"it", de_prob:"de", fr_prob:"fr"}
    max_prob = max(prob_dict.keys())
    if max_prob < 0:
        word_lang = 'en'
    else:
        word_lang = prob_dict[max_prob]
    return word_lang


print(process('catalano'))
