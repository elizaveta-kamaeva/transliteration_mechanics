from time import time
from Mechanics import get_word
import NaiveRepl
import LanguageDetector
import SpecRepl


infile_name = 'texts/translit-cosmetics.csv'
outfile_name = 'texts/translit-cosmetics-new.txt'
infile = open(infile_name, 'r', encoding='utf-8')
outfile = open(outfile_name, 'w', encoding='utf-8')

# for reporting
file_size = 1481
n = 0
naive_trans_processing = 0.0
language_detector_processing = 0.0
specific_trans_processing = 0.0
total_processing = time()

# preparing output
outfile.write('raw_word;naive_trans;spec_trans;\n')
print('Progress:')

# start working
for line in infile:
    raw_word, word = get_word(line)
    # if the line is empty, take another line
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

    #outfile.write('{};{};{};\n'.format(raw_word, naive_trans, spec_trans))
    outfile.write('{} - {}; {} - {}\n'.format(raw_word, naive_trans, language, spec_trans))

    # progress report
    n += 1
    if n % 100 == 0:
        progress = round(n / file_size * 100)
        print('{}{}% done'.format('|'*round(progress/4), progress))

infile.close()
outfile.close()
total_processing = time() - total_processing

print("I've finished.")
print('Naive Replacer worked for {} seconds'.format(naive_trans_processing))
print('Language Detector worked for {} seconds'.format(language_detector_processing))
print('Specific Translator worked for {} seconds'.format(specific_trans_processing))
print('Total working time: {} seconds'.format(total_processing))
