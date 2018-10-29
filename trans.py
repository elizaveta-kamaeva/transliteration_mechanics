from sys import argv
import Processor

for file_path in argv[1:]:
    Processor.process('texts\\' + file_path)

#Processor.process('texts\\new-brands-mirbeer.txt')
