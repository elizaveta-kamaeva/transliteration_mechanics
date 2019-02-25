'''
from . import FranRepl
from . import ItaRepl
from . import GerRepl
from . import JapRepl
from . import EngRepl
from . import LatRepl
'''
from language_modules import EngRepl, FranRepl, GerRepl, ItaRepl, JapRepl, LatRepl


def delegator(lang, word):
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
    return trans_word
 
