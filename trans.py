from sys import argv
from time import time

import Processor

total_processing = time()
for infile_path in argv[1:]:
    infile = open('texts\\' + infile_path, 'r', encoding='utf-8')
    raw_lines = infile.readlines()
    infile.close()

    eng_file = open('eng_trans.txt', 'r', encoding='utf-8')
    ready_lines, n, periods = Processor.process(raw_lines, eng_file.readlines())
    eng_file.close()

    outfile = open('texts\\' + infile_path.replace('.csv', '-trans.csv'), 'w', encoding='utf-8')
    outfile.write('brand,alias\n')

    for word_pair in ready_lines:
        outfile.write(','.join(word_pair) + '\n')
    outfile.close()

    naive_trans_processing = periods[0]
    language_detector_processing = periods[1]
    specific_trans_processing = periods[2]
    total_processing = time() - total_processing

    print("I've finished.")
    print('Number of lines processed:', n)
    print('Naive Replacer worked for {} seconds'.format(naive_trans_processing))
    print('Language Detector worked for {} seconds'.format(language_detector_processing))
    print('Specific Translator worked for {} seconds'.format(specific_trans_processing))
    print('Total working time: {} seconds'.format(total_processing))
    print('Speed: {} words per second'.format(round(n / total_processing)))