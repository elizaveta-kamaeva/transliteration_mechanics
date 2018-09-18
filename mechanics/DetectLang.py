import re


def trail(word, ngrams, maygrams, stopgrams):
    lang_prob = 0
    # searching for stop-ngrams
    for stopgram in stopgrams:
        stopgram = re.sub(r'\\A', r'(\\s|^)', stopgram)
        stopgram = re.sub(r'\\Z', r'(\\s|$|-)', stopgram)
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
        maygram = re.sub(r'\\A', r'(\\s|^)', maygram)
        maygram = re.sub(r'\\Z', r'(\\s|$|-)', maygram)
        found_maygrams = re.findall(maygram, word)
        if found_maygrams:
            lang_prob += 0.5
    return lang_prob
