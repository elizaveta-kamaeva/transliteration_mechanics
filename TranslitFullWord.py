'''
from .mechanics.Getter import get_word
from . import NaiveRepl
from . import LanguageDetector
from . import SpecRepl
'''
from langage_modules import NaiveRepl
from mechanics import SpecRepl
import LanguageDetector



def translit(word):
    # naive translit
    naive_trans = NaiveRepl.process(word)

    # defining the language
    language = LanguageDetector.process(word)

    # translit in a specific language
    spec_trans = SpecRepl.delegator(language, word)

    if naive_trans != spec_trans:
        return [spec_trans, naive_trans]
    else:
        return [spec_trans]


existing_words = set()
def transer(word):
    global existing_words

    # if the line is inappropriate, take another line
    if not word or word in existing_words:
        return None

    transes = []
    # naive translit
    naive_trans = NaiveRepl.process(word)

    # defining the language
    language = LanguageDetector.process(word)

    # translit in a specific language
    spec_trans = SpecRepl.delegator(language, word)

    # add translit
    if not naive_trans in existing_words:
        existing_words.add(naive_trans)
        transes.append(naive_trans)

        if spec_trans != naive_trans:
            existing_words.add(spec_trans)
            transes.append(spec_trans)

    return transes
