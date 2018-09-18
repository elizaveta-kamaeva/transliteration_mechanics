import re


def replacer(word_string, literals_dict):
    word_list = word_string.split()
    prev_len = 0
    toreplace_list = []
    # replacing the needed ngrams
    for i in range(len(word_list)):
        word = word_list[i]
        for literal in literals_dict:
            ngrams_found = re.finditer(literal, word)
            if not ngrams_found:
                continue
            for match_obj in ngrams_found:
                pos = match_obj.span()
                repl_tuple = (literals_dict[literal],
                              [p + prev_len for p in pos], pos[1] - pos[0])
                toreplace_list.append(repl_tuple)
        prev_len += len(word)
    return toreplace_list



def repl(word,
         short_ngrams_replaced = None,
         literals_replaced = None,
         words_replaced = None,
         long_ngrams_replaced = None,
         condit_ngrams_replaced = None):
    replace_arrays = [words_replaced,
                 long_ngrams_replaced,
                 condit_ngrams_replaced,
                 short_ngrams_replaced,
                 literals_replaced]
    repled_list = [''*len(word)]
    i = 0
    while i != len(replace_arrays):
        # delete empty replace arrays
        if replace_arrays[i] == None:
            del replace_arrays[i]
        else:
            i += 1
    letter_list = list(word)
    for toreplace_list in replace_arrays:
        # each single replace array equals to-replace list
        # to-replace list = [(repl_tuple), (repl_tuple), ...]
        if not toreplace_list:
            continue
        for repl_tuple in toreplace_list:
            # repl_tuple = (repl_str=[xxx], pos=(0,2), len=2)
            repl_str = repl_tuple[0]
            pos = repl_tuple[1]
            repl_len = repl_tuple[2]
            # if the fragment has already been replaced, then skip
            if letter_list[pos[0]] != '':
                continue
            # e.g. i -> ай
            if repl_len < len(repl_str):
                repled_list = list(repl_str[:repl_len]).extend(list(repl_str[repl_len:]))
            # e.g. tion -> шн
            elif repl_len > len(repl_str):
                repled_list = list(repl_str[:repl_len]).extend([' '*(repl_len-len(repl_str))])
            # e.g. n -> н
            else:
                repled_list = list(repl_str)
            # insert letters into the final list
            for j in range(len(repled_list)):
                letter_list[j] = repled_list[j]
    final_word = ''.join(letter_list).strip()
    print(final_word)
    return final_word

# Непонятно, как справляться вот с этой ситуацией
# scholl -> шолль
# sch - ш
# ch - x


# repl_tuple = (repl_str=[xxx], pos=(0,2), len=2)
# (0,2), (4,7)
# (1,4)
# (0,1), (1,2), (2,3) ...
# (0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7)
# (x__), (xx_), (___), (___), (x__), ( __), ( __)
# (x__), (xx_), (___), (___), (x__), ( __), ( __)
# (x__), (xx_), (z__), (z__), (x__), ( __), ( __)

'''
        for literal in literals_dict:
            word_list[i] = re.sub(literal, literals_dict[literal], word_list[i])
        
    new_string = ' '.join(word_list)
    return new_string
'''
