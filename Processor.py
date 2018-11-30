from mechanics.Getter import get_word
import NaiveRepl
import LanguageDetector
import SpecRepl


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


def process(raw_lines):
    ready_pairs = []

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
        if not word:
            continue

        # naive translit
        naive_trans, naive_time = NaiveRepl.process(word)
        naive_trans_processing += naive_time

        # defining the language
        language, lang_time = LanguageDetector.process(word)
        language_detector_processing += lang_time

        # translit in a specific language
        spec_trans, spec_time = SpecRepl.delegator(language, word)
        specific_trans_processing += spec_time

        # write the pairs into a set
        ready_pairs.append((raw_word, naive_trans, language))
        if naive_trans != spec_trans:
            ready_pairs.append((raw_word, spec_trans, language))

        # progress report each 200 lines
        n += 1
        if n % 200 == 0:
            print('{} lines done'.format(n))

    return ready_pairs, n, [naive_trans_processing,
                            language_detector_processing,
                            specific_trans_processing]
