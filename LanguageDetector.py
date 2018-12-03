import re
from time import time
from mechanics.DetectLang import trail


def it_trailer(word):
    it_ngrams = {'\A([^euioay-][uioa])+\Z',
                 'c[euioa]\w*c[euioa]',
                 'zz\w*[euioa]\Z', 'cc\w*[euioa]\Z', 'tt\w*[euioa]\Z',
                 'pp\w*[euioa]\Z', 'll\w*[euioa]\Z', 'ss\w*[euioa]\Z',
                 'rr\w*[euioa]\Z', 'cch\w+',
                 '\Adi\Z', '\Ail\Z'}

    it_maygrams = {'[euioa]c[euioa]\w*[euioa]\Z',
                   'z\w*[euioa]\Z'}

    it_stopgrams = {'[^euioayzctplsr]{3}', 'up', '[^euioay]\Z'}

    it_prob = trail(word, it_ngrams, it_maygrams, it_stopgrams)
    return it_prob


def jp_trailer(word):
    jp_ngrams = {'\A([^euioay -][euioa])+\Z',
                 '\Aya', '\Ayo', '\Ayu', 'tsu',
                 '([euioa]|\A)j[euioa]'}

    jp_maygrams = {'wa', 'wo', '([euioa]|\A)ke',
                   '([euioa]|\A)ka', '([euioa]|\A)ku',
                   '([euioa]|\A)ko', '([euioa]|\A)ki',
                   '([euioa]|\A)shi',
                   'ya', 'yo', 'ya', 'yu'}

    jp_stopgrams = {'[^euioatsh]{2}',
                    '[^uioa]\Z', 'c[^h]', 'y[^aou]',
                    'x', 'v', 'q'}
    jp_prob = trail(word, jp_ngrams, jp_maygrams, jp_stopgrams)
    return jp_prob


def de_trailer(word):
    de_ngrams = {'(ch|sh|ff)\w+(ch|sh|ff)',
                 '[^euioa \'-]{4}',
                 'sch', 'chs', 'ß', 'ö', 'ä', 'ü',
                 '[^euioay -]st', 'ung\Z', '\Aein',
                 '\Adie\Z', '\Adas\Z', '\Ader\Z',
                 'mann\Z', 'gut', 'burg'}

    de_maygrams = {'[euioa]{2}.*[^eouia \'-]{3}.*[eouia]{2}',
                   '[^euioa(ch) \'-]{3}\Z', 'rau\Z',
                   '[^euioay -]en\Z', '[^euioay -]ern\Z',
                   '[^euioay -]z', 'z[^euioay -]',
                   'eich', 'ein'}

    de_stopgrams = {'x', 'y', 'tion', '[eiaou]{3}\Z', 'light'}

    de_prob = trail(word, de_ngrams, de_maygrams, de_stopgrams)
    return de_prob


def fr_trailer(word):
    fr_ngrams = {'[euioa]{3}',
                 '[euioa]{2}\w+[euioa]{2}\w',
                 'ouch', 'eur', 'ance', 'agne\Z',
                 'ngie\Z', 'gn\w{2}\Z', 'oix\Z', 'ux\Z', 'oir\Z',
                 "\Ad'", "\Al'", '\Ala\Z', '\Ale\Z',
                 'bell', 'lacoste',
                 '\A?les\Z', '\Ale\Z', '\Adu\Z', '\Ade\Z', '\Aet\Z',
                 'é', 'è', 'à', 'ù', 'que',
                 'ê', 'â', 'ô', 'î', 'û',
                 'ë', 'ï', 'ü', 'ÿ', 'ç', 'à'}

    fr_maygrams = {'\Ala\w+[euioay]{2}', 'gue',  '\wou(?!gh)', 'ou[^euioa -][euioa][^euioa]\Z',
                   'ch\w*[euioay]{2}', 'au\Z', 'que'}

    fr_stopgrams = {'sh', 'w', 'you', 'house', 'round'}

    fr_prob = trail(word, fr_ngrams, fr_maygrams, fr_stopgrams)
    return fr_prob


def lat_trailer(word):
    lat_ngrams = {'a\Z', 'u[ms]\Z', 'ae\Z'}

    lat_maygrams = {'c', 'x'}

    lat_stopgrams = {'sh', 'w',
                     'é', 'è', 'à', 'ù', 'que',
                     'ê', 'â', 'ô', 'î', 'û',
                     'ë', 'ï', 'ü', 'ÿ', 'ç', 'à'}

    lat_prob = trail(word, lat_ngrams, lat_maygrams, lat_stopgrams)
    return lat_prob


def process(word):
    start_time = time()
    word = re.sub('\d+([-\',.]\d+)?', '', word)
    prob_list = [it_trailer(word), de_trailer(word),
                 fr_trailer(word), jp_trailer(word),
                 lat_trailer(word)]
    lang_list = ['ita', 'ger', 'fra', 'jap', 'lat']
    max_prob = max(prob_list)
    if max_prob < 1:
        word_lang = 'en'
    else:
        word_lang = lang_list[prob_list.index(max_prob)]
    duration = time() - start_time
    return word_lang, duration
