import re
from time import time


def trail(word, ngrams, maygrams, stopgrams):
    lang_prob = 0
    # searching for stop-ngrams
    for stopgram in stopgrams:
        found_stopgrams = re.findall(stopgram, word)
        if found_stopgrams:
            return 0

    # searching for undisputable ngrams
    for ngram in ngrams:
        ngram = re.sub(r'\\A', r'(\\s|^)', ngram)
        ngram = re.sub(r'\\Z', r'(\\s|$|-)', ngram)
        found_ngrams = re.findall(ngram, word)
        if found_ngrams:
            lang_prob += 1

    # searching for possible language ngrams
    for maygram in maygrams:
        found_maygrams = re.findall(maygram, word)
        if found_maygrams:
            lang_prob += 0.5
    return lang_prob



def it_trailer(word):
    it_ngrams = {'\A([^euioay-][euioa])+\Z',
                 'zz\w*[euioa]\Z', 'cc\w*[euioa]\Z', 'tt\w*[euioa]\Z',
                 'pp\w*[euioa]\Z', 'll\w*[euioa]\Z', 'ss\w*[euioa]\Z',
                 'rr\w*[euioa]\Z', 'cch\w+',
                 '\Adi\Z', '\Ail\Z'}

    it_maygrams = {'[euioa]c[euioa]\w*[euioa]\Z',
                   'z\w*[euioa]\Z'}

    it_stopgrams = {'[^euioay]{3}', 'up'}

    it_prob = trail(word, it_ngrams, it_maygrams, it_stopgrams)
    return it_prob


def de_trailer(word):
    de_ngrams = {'(ch|sh|ff)\w+(ch|sh|ff)',
                 'sch', 'chs', 'ß', 'ö', 'ä', 'ü',
                 '[^euioay-]st', 'ung\Z', '\Aein',
                 '\Adie\Z', '\Adas\Z', '\Ader\Z',
                 'mann\Z', 'gut', 'burg'}

    de_maygrams = {'[euioa]{2}.*[^eouia-]{3}.*[eouia]{2}',
                   '[^euioa-]{4}',
                   '[^euioay-]en\Z', '[^euioay-]ern\Z',
                   '[^euioay-]z', 'z[^euioay-]',
                   'eich', 'z'}

    de_stopgrams = {'x', 'y', 'tion', '[eiaou]{2}\Z'}

    de_prob = trail(word, de_ngrams, de_maygrams, de_stopgrams)
    return de_prob


def fr_trailer(word):
    fr_ngrams = {'[euioa]{3}',
                 'ouch', 'eur', 'ance', '\wou(?!gh)',
                 'ngie\Z', 'gnie\Z', 'oix\Z', 'ux\Z', 'oir\Z',
                 "\Ad'", "\Al'", '\Ala\Z', '\Ale\Z', 'bell',
                 '\A?les\Z', '\Ale\Z', '\Adu\Z', '\Ade\Z',
                 'é', 'è', 'à', 'ù', 'que',
                 'ê', 'â', 'ô', 'î', 'û',
                 'ë', 'ï', 'ü', 'ÿ', 'ç'}

    fr_maygrams = {'ch\w*[euioay]{2}', '\Ala\w+[euioay]{2}',
                   'au\Z'}

    fr_stopgrams = {'sh', 'w', 'you', 'house', 'round'}

    fr_prob = trail(word, fr_ngrams, fr_maygrams, fr_stopgrams)
    return fr_prob


def process(word):
    start_time = time()
    prob_list = [it_trailer(word), de_trailer(word), fr_trailer(word)]
    lang_list = ['fra', 'ita', 'ger']
    max_prob = max(prob_list)
    if max_prob < 1:
        word_lang = 'en'
    else:
        word_lang = lang_list[prob_list.index(max_prob)]
    duration = time() - start_time
    return word_lang, duration
