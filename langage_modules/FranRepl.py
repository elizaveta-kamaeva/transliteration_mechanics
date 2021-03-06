from collections import OrderedDict
#from .mechanics.Repl import replacer
from mechanics.Repl import replacer


def trans_long_ngrams(word):
    long_ngrams_dict = OrderedDict({
        'eaux\Z':'о', 'beaut':'бьют', 'eau':'о', 'ogne\Z':'он',
        'gnie':'йн', 'agne':'ейн', 'ouge':'уж', 'oix':'уа', 'iei':'ье',
        'oux':'о', '(?<=\w)qu[eéè]\Z':'к', 'ch':'ш'})
    new_word = replacer(word, long_ngrams_dict)
    return new_word


def trans_conditional(word):
    condit_ngrams_dict = OrderedDict({
        '\Ales\Z':'ле', '\Ac':'к',
        '\A[eéè](?![euioayéèàù-])':'э',
        '\Aeu':'ев', 'u[eéè]u':'е',
        'ieu\Z':'ью',
        'u[eéè]\Z':'ью', 'gi[eéè]\Z':'ж',
        'nc[eéè]\Z':'нс',
        'g\Z':'ж','z\Z':'ц', 'y\Z':'и',
        'tion(?=\w?\Z)':'шн',
        'g(?=[ieyéè])':'ж',
        'ai(?=[^euioayéèàù-]{2})':'е',
        'l[eéè]':'ле', 'l[uù]':'лю',
        '(?<=[euioayéèàù])x{?=[euioayéèàù]\w+}':'кз',
        '(?<=[euioayéèàù])s(?=[euioayéèàù])':'з',
        '(?<=\w{3})[e]\Z':'',
        '(?<=[rdgkzb])h(?!\Z)':''})
    new_word = replacer(word, condit_ngrams_dict)
    return new_word


def trans_short_ngrams(word):
    short_ngrams_dict = OrderedDict({
        'ph':'ф', 'qu':'кв', 'sc':'ск', 'cs':'кс', 'th':'т',
        'oi':'уа', 'ou':'у', 'ay':'ей', 'ie':'ье'})
    new_word = replacer(word, short_ngrams_dict)
    return new_word


def trans_literals(word):
    literal_dict = {
        'b':'б', 'c':'к', 'd':'д', 'f':'ф', 'g':'г',
        'h':'х', 'j':'ж', 'k':'к', 'l':'л', 'm':'м',
        'n':'н', 'p':'п', 'q':'к', 'r':'р', 's':'с',
        't':'т', 'v':'в', 'w':'в', 'x':'кс', 'z':'з',
        'a':'а', 'e':'е', 'i':'и', 'o':'о', 'u':'у',
        'y':'и', 'é':'е', 'è':'е', 'à':'а', 'ù':'у',
        'ê':'е', 'â':'а', 'ô':'о', 'î':'и', 'û':'у',
        'ë':'е', 'ï':'и', 'ü':'у', 'ÿ':'и', 'ç':'с'}
    new_word = replacer(word, literal_dict)
    return new_word


def process(word):
    long_ngrams_replaced = trans_long_ngrams(word)
    condit_ngrams_replaced = trans_conditional(long_ngrams_replaced)
    short_ngrams_replaced = trans_short_ngrams(condit_ngrams_replaced)
    literals_replaced = trans_literals(short_ngrams_replaced)
    return literals_replaced
