from sys import argv
import Processor

for file_path in argv[1:]:
    if 'translit' not in file_path:
        continue
    Processor.process(file_path)

#Processor.process('texts\\brands-electronics.txt')
