def process(raw_str, trans_str, existing_words):
    sg_words_pairs = []
    raw_list = raw_str.split()
    trans_list = trans_str.split()
    if len(raw_list) == len(trans_list):
        for i in range(len(raw_list)):
            eng_word = raw_list[i]
            rus_word = trans_list[i]
            if len(eng_word) > 2 and not rus_word in existing_words:
                existing_words.add(rus_word)
                sg_words_pairs.append((eng_word, rus_word))
    return sg_words_pairs, existing_words