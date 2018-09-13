from time import time
import FranRepl
import ItaRepl
import GerRepl
import EngRepl


def delegator(lang, word):
    start_time = time()
    if lang == 'fra':
        trans_word = FranRepl.process(word)
    elif lang == 'ita':
        trans_word = ItaRepl.process(word)
    elif lang == 'ger':
        trans_word = GerRepl.process(word)
    else:
        trans_word = EngRepl.process(word)
    duration = time() - start_time
    return trans_word, duration
 
