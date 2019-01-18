from sys import argv
from time import time
import re

from TranslitFullWord import transer
from Separator import separate_words
from mechanics.Getter import get_raw, get_word2process


def get_lines(infile_path):
    # get lines with brands from a file
    infile = open('texts\\' + infile_path, 'r', encoding='utf-8')
    raw_lines = infile.readlines()
    infile.close()
    return raw_lines


def get_transes(raw_lines):
    # produce translit
    ready_dict = {}
    n = 0
    for line in raw_lines:
        raw_word = get_raw(line)
        word = get_word2process(line)
        transes = transer(word)
        if transes:
            for trans in transes:
                ready_dict[trans] = raw_word

                # get translit for a singular word
                sg_transes = separate_words(word, trans, set(ready_dict.keys()))
                if sg_transes:
                    for sg_trans in sg_transes.keys():
                        ready_dict[sg_trans] = sg_transes[sg_trans]

        # progress report each 200 lines
        n += 1
        if n % 200 == 0:
            print('{} lines done'.format(n))
    return ready_dict


def write_transes(trans_dict, infile_path):
    # write translit into a file
    outfile = open('texts\\' + re.sub('\.(txt|csv)$', '-trans.csv', infile_path), 'w', encoding='utf-8')
    outfile.write('brand\talias\n')

    for word in trans_dict.keys():
        outfile.write('{0}\t{1}\n'.format(trans_dict[word], word))
    outfile.close()


total_processing = time()
lines = []
for infile_path in argv[1:]:
# for infile_path in ['test_words.txt']:
    print('Progress:')
    lines = get_lines(infile_path)
    trans_dict = get_transes(lines)
    write_transes(trans_dict, infile_path)

    print("I've finished.")
    print('Number of lines processed:', len(lines))
    print('Total working time: {} seconds'.format(total_processing))
    print('Speed: {} words per second'.format(round(len(lines) / (time() - total_processing))))
