from time import time
import re
import NaiveRepl
import LanguageDetector
from Delegator import delegator


infile_name = 'sport-translit.csv'
outfile_name = 'sport-translit-new.csv'
infile = open(infile_name, 'r', encoding='utf-8')
outfile = open(outfile_name, 'w', encoding='utf-8')

# for reporting
file_size = 2000
num_modules = 2
# for time calculation
n = 0
naive_trans_processing = 0.0
language_detector_processing = 0.0
specific_trans_processing = 0.0
total_processing = time()

# preparing output
outfile.write('old_trans;eng_word;new_trans\n')
print('Progress:')

for line in infile:
    old_trans, raw_word = line.split(';')
    # stripping spaces and punctuation
    raw_word = raw_word.strip()
    raw_word = raw_word.lower()
    word = re.search('[\w&].*[\w&]', raw_word)
    try:
          word = word.group()
    except:
          print('The string "{}" is empty '
                'or less than 2 characters.'.format(raw_word))
          continue

    # naive translit
    naive_trans, naive_time = NaiveRepl.process(word)
    naive_trans_processing += naive_time

    # defining the language
    language, lang_time = LanguageDetector.process(word)
    language_detector_processing += lang_time

    # translit in a specific language
    spec_trans, spec_time = delegator(language, word)
    specific_trans_processing += spec_time

    outfile.write('{};{};{};\n'.format(old_trans, word, naive_trans))

    # progress report
    n += 1
    if n % 100 == 0:
        progress = round(n / file_size * 100 / num_modules)
        print('{}{}% done'.format('|'*round(progress/2), progress))

infile.close()
outfile.close()
total_processing = time() - total_processing

print("I've finished.")
print('Naive Replacer worked for {} seconds'.format(naive_trans_processing))
print('Language Detector worked for {} seconds'.format(language_detector_processing))
print('Specific Translator worked for {} seconds'.format(specific_trans_processing))
print('Total working time: {} seconds'.format(total_processing))
