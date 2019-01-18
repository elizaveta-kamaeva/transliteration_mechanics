from TranslitMaker import trans_full_string, trans_separate


def get_transes(word_dict):
    ready_dict = {}
    n = 0
    for raw_word in word_dict.keys():
        word = word_dict[raw_word]
        transes = trans_full_string(word)
        if transes:
            for trans in transes:
                ready_dict[trans] = raw_word

                # get translit for a singular word
                sg_transes = trans_separate(word, trans, set(ready_dict.keys()))
                if sg_transes:
                    for sg_trans in sg_transes.keys():
                        ready_dict[sg_trans] = sg_transes[sg_trans]

        # progress report each 200 lines
        n += 1
        if n % 200 == 0:
            print('{} lines done'.format(n))

    return ready_dict
