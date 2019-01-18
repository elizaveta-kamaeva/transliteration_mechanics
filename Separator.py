import re


def separate_words(raw_str, trans_str, existing_words):
    sg_words = {}
    raw_list = re.split('[\s.-]', raw_str)
    trans_list = re.split('[\s.-]', trans_str)
    if len(raw_list) == len(trans_list):
        for i in range(len(raw_list)):
            eng_word = raw_list[i]
            rus_word = trans_list[i]
            if len(rus_word) > 2 and rus_word not in existing_words:
                sg_words[rus_word] = eng_word

        return sg_words

