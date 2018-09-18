from mechanics.Repl import replacer


def trans_short_ngrams(word):
    short_ngrams_dict = {
        'sh':'ш', 'ts':'ц', 'ya':'я', 'yo':'е', 'yu':'ю',
        'aa':'а', 'ee':'е', 'uu':'у', 'ii':'и', 'oo':'о'}
    new_word = replacer(word, short_ngrams_dict)
    return new_word


def trans_literals(word):
    literal_dict = {
        'b':'б', 'd':'д', 'f':'ф', 'g':'г',
        'h':'х', 'j':'дж', 'k':'к', 'l':'л',
        'm':'м', 'n':'н', 'p':'п', 'r':'р',
        's':'с', 't':'т', 'w':'в', 'z':'з',
        'a':'а', 'e':'е', 'i':'и', 'o':'о', 'u':'у'}
    new_word = replacer(word, literal_dict)
    return new_word


def process(word):
    short_ngrams_replaced = trans_short_ngrams(word)
    literals_replaced = trans_literals(short_ngrams_replaced)
    return literals_replaced
