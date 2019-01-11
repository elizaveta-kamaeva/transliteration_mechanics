from EngRepl import process

new_word = process(input('Tested word: '))
while new_word:
    print(new_word)
    new_word = process(input('Tested word: '))
