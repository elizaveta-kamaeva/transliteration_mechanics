from sys import argv
import Processor

for infile_path in argv[1:]:
    outfile_path = infile_path.replace('.csv', '-trans.csv')
    Processor.process('texts\\' + infile_path, 'texts\\' + outfile_path)

#Processor.process('texts\\new-brands-mirbeer.txt')
