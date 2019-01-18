from sys import argv
from time import time
import re

from TransCollector import get_transes
from mechanics.Getter import get_raw, get_word2process


def get_lines(infile_path):
    # get lines with brands from a file
    infile = open('texts\\' + infile_path, 'r', encoding='utf-8')
    raw_lines = infile.readlines()
    infile.close()
    return raw_lines


def get_word(lines):
    # gets a raw word and a word to process further
    word_dict = {}
    for line in lines:
        raw_word = get_raw(line)
        word = get_word2process(line)
        word_dict[raw_word] = word
    return word_dict


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
    print('Progress:')
    lines = get_lines(infile_path)
    words = get_word(lines)
    trans_dict = get_transes(words)
    write_transes(trans_dict, infile_path)

    print("I've finished.")
    print('Number of lines processed:', len(lines))
    print('Total working time: {} seconds'.format(total_processing))
    print('Speed: {} words per second'.format(round(len(lines) / (time() - total_processing))))
