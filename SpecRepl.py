from time import time
import FranRepl
import ItaRepl
import GerRepl
import JapRepl
import EngRepl


def delegator(lang, word, eng_repls):
    start_time = time()
    word = word.replace("'", '')
    if lang == 'fra':
        trans_word = FranRepl.process(word)
    elif lang == 'ita':
        trans_word = ItaRepl.process(word)
    elif lang == 'ger':
        trans_word = GerRepl.process(word)
    elif lang == 'jap':
        trans_word = JapRepl.process(word)
    else:
        trans_word = EngRepl.process(word, eng_repls)
    duration = time() - start_time
    return trans_word, duration
 
