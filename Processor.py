from mechanics.Getter import get_word
import NaiveRepl
import LanguageDetector
import SpecRepl


def process(raw_lines, eng_repls):
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

        existing_words.add(raw_word)
        # naive translit
        naive_trans, naive_time = NaiveRepl.process(word)
        naive_trans_processing += naive_time

        # defining the language
        language, lang_time = LanguageDetector.process(word)
        language_detector_processing += lang_time

        # translit in a specific language
        spec_trans, spec_time = SpecRepl.delegator(language, word, eng_repls)
        specific_trans_processing += spec_time

        # write the pairs into a set
        '''
        ready_pairs.append((raw_word, naive_trans))
        if naive_trans != spec_trans:
            ready_pairs.append((raw_word, spec_trans, language))
        '''
        ready_pairs.append((raw_word, spec_trans, language))
        # progress report each 200 lines
        n += 1
        if n % 200 == 0:
            print('{} lines done'.format(n))

    return ready_pairs, n, [naive_trans_processing,
                            language_detector_processing,
                            specific_trans_processing]
