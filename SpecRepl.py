from time import time
from . import FranRepl
from . import ItaRepl
from . import GerRepl
from . import JapRepl
from . import EngRepl
from . import LatRepl
'''
import FranRepl
import ItaRepl
import GerRepl
import JapRepl
import EngRepl
import LatRepl
'''


def delegator(lang, word):
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
    elif lang == 'lat':
        trans_word = LatRepl.process(word)
    else:
        trans_word = EngRepl.process(word)
    duration = time() - start_time
    return trans_word, duration
 
