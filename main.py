from time import time
from mechanics.Getter import get_word
import NaiveRepl
import LanguageDetector
import SpecRepl


infile_name = 'texts/translit-food-rest.csv'
outfile_name = 'texts/translit-food-new2.txt'
infile = open(infile_name, 'r', encoding='utf-8')
outfile = open(outfile_name, 'w', encoding='utf-8')
eng_file = open('eng_trans.txt', 'r', encoding='utf-8')

# for reporting
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
    spec_trans, spec_time = SpecRepl.delegator(language, word, eng_file)
    specific_trans_processing += spec_time

    #outfile.write('{};{};{};\n'.format(raw_word, naive_trans, spec_trans))
    outfile.write('{} - {}; {} - {}\n'.format(raw_word, naive_trans, language, spec_trans))

    # progress report each 5%
    n += 1
    if n % 200 == 0:
        print('{} lines done'.format(n))

infile.close()
outfile.close()
eng_file.close()
total_processing = time() - total_processing

print("I've finished.")
print('Number of lines processed:', n)
print('Naive Replacer worked for {} seconds'.format(naive_trans_processing))
print('Language Detector worked for {} seconds'.format(language_detector_processing))
print('Specific Translator worked for {} seconds'.format(specific_trans_processing))
print('Total working time: {} seconds'.format(total_processing))
print('Speed: {} words per second'.format(round(n / total_processing)))
