import Processor


tail = '123;'
new_word = Processor.process([tail + input('Tested word: ')])
while new_word:
    print(new_word)
    new_word, _, _ = Processor.process([tail + input('Tested word: ')])
