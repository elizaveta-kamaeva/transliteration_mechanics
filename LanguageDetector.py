import re
from time import time


def it_trailer(word):
    it_ngrams = {'zz\w*[euioa]\Z', 'cc\w*[euioa]\Z', 'tt\w*[euioa]\Z',
                 'pp\w*[euioa]\Z', 'll\w*[euioa]\Z', 'ss\w*[euioa]\Z',
                 'rr\w*[euioa]\Z', 'z\w*[euioa]\Z',
                 '[euioa]c[euioa]\w*[euioa]\Z',
                 '\A([^euioay-][euioa])+\Z',
                 'cch\w+', '\Adi\Z'}
    for ngram in it_ngrams:
        ngram = re.sub(r'\\A', r'(\\s|^)', ngram)
        ngram = re.sub(r'\\Z', r'(\\s|$|-)', ngram)
        found_ngrams = re.findall(ngram, word)
        if found_ngrams:
            return 1
    return 0


def de_trailer(word):
    de_ngrams = {'(ch|sh|ff)\w+(ch|sh|ff)',
                 'sch', 'chs', 'ß',
                 'z[^euioay-]', '[^euioay-]z', '[^euioay-]st',
                 'en\Z', 'ern\Z', 'ung\Z'}
    de_neg_ngrams = {'x', 'y'}
    # searching for stop-ngrams
    for neg_ngram in de_neg_ngrams:
        found_neg_ngrams = re.findall(neg_ngram, word)
        if found_neg_ngrams:
            return 0

    for ngram in de_ngrams:
        ngram = re.sub(r'\\A', r'(\\s|^)', ngram)
        ngram = re.sub(r'\\Z', r'(\\s|$|-)', ngram)
        found_ngrams = re.findall(ngram, word)
        if found_ngrams:
            return 1
    return 0


def fr_trailer(word):
    fr_ngrams = {'[euioa]{3}', '\Ala\w+[euioay]{2}',
                 'ch\w*[euioay]{2}',
                 'ouch', 'eur', '\wou(?!gh)',
                 'ngie\Z', 'gnie\Z', 'oix\Z',
                 'ux\Z', 'que', 'au\Z',
                 "\Ad'", "\Al'",
                 '\Ales\Z', '\Ale\Z', '\Adu\Z', '\Ade\Z',
                 '\Ala\Z', '\Ale\Z'}
    fr_neg_ngrams = {'sh', 'w', 'you'}
    # searching for stop-ngrams
    for neg_ngram in fr_neg_ngrams:
        found_neg_ngrams = re.findall(neg_ngram, word)
        if found_neg_ngrams:
            return 0
    # searching for needed ngrams
    for ngram in fr_ngrams:
        ngram = re.sub(r'\\A', r'(\\s|^)', ngram)
        ngram = re.sub(r'\\Z', r'(\\s|$|-)', ngram)
        found_ngrams = re.findall(ngram, word)
        if found_ngrams:
            return 1
    return 0


def process(word):
    start_time = time()
    it_prob = it_trailer(word)
    de_prob = de_trailer(word)
    fr_prob = fr_trailer(word)
    prob_list = [fr_prob, it_prob, de_prob]
    lang_list = ['fra', 'ita', 'ger']
    max_prob = max(prob_list)
    if max_prob < 1:
        word_lang = 'en'
    else:
        word_lang = lang_list[prob_list.index(max_prob)]
    duration = time() - start_time
    return word_lang, duration

