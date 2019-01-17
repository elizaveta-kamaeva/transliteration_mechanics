'''
from .mechanics.Getter import get_word
from .mechanics import Separator, SpecRepl
from . import NaiveRepl
from . import LanguageDetector
from . import SpecRepl
'''
from mechanics.Getter import get_word
from mechanics import Separator, SpecRepl
import NaiveRepl
import LanguageDetector


def translit(word):
    # naive translit
    naive_trans, _ = NaiveRepl.process(word)

    # defining the language
    language, _ = LanguageDetector.process(word)

    # translit in a specific language
    spec_trans, _ = SpecRepl.delegator(language, word)

    if naive_trans != spec_trans:
        return [spec_trans, naive_trans]
    else:
        return [spec_trans]


existing_words = set()
def process(raw_lines):
    ready_pairs = []
    existing_words = set()

    # for reporting
    n = 0
    naive_trans_processing = 0.0
    language_detector_processing = 0.0
    specific_trans_processing = 0.0
    print('Progress:')

    # start working
    for line in raw_lines:
        raw_word, word = get_word(line)
        # if the line is inappropriate, take another line
        if not word or word in existing_words:
            continue
        else:
            existing_words.add(raw_word)

        # naive translit
        naive_trans, naive_time = NaiveRepl.process(word)
        naive_trans_processing += naive_time

        # defining the language
        language, lang_time = LanguageDetector.process(word)
        language_detector_processing += lang_time

        # translit in a specific language
        spec_trans, spec_time = SpecRepl.delegator(language, word)
        specific_trans_processing += spec_time

        # writing words into a list
        if not naive_trans in existing_words:
            existing_words.add(naive_trans)
            # write naive translit
            ready_pairs.append((raw_word, naive_trans))
            # write naive translit for each word separately
            words_by_one_naive, existing_words = Separator.process(raw_word, naive_trans, existing_words)
            ready_pairs.extend(words_by_one_naive)

            if naive_trans != spec_trans and not spec_trans in existing_words:
                # write special translit
                existing_words.add(spec_trans)
                ready_pairs.append((raw_word, spec_trans))
                # write special translit for each word separately
                words_by_one_spec, existing_words = Separator.process(raw_word, spec_trans, existing_words)
                ready_pairs.extend(words_by_one_spec)

        # progress report each 200 lines
        n += 1
        if n % 200 == 0:
            print('{} lines done'.format(n))

    return ready_pairs, n, [naive_trans_processing,
                            language_detector_processing,
                            specific_trans_processing]
