#!/usr/bin/python3
import argparse

class File:
    def __init__(self, filename):
        self.translated = ""
        self.load_file(filename)

 
    def run(self):
        '''
        runs translated file
        '''
        #print(self.translated)
        exec(self.translated)

    def load_file(self, filename):
        '''
        reads in file, translating line by line, 
        storing back into self.file_strings
        '''

        with open(filename, "r") as file:
            for line in file:
                new_line, l_space = File.strip_spaces(line)
                new_line = new_line.strip() 
                new_line = File.translate(new_line)
                new_line = File.add_spaces(new_line, l_space)
                self.translated += new_line + ";\n"
    
    @staticmethod
    def strip_spaces(line):
        '''
        removes and counts leading and trailing spaces
        '''
        l_space = len(line)
        line = line.lstrip()
        new_length = len(line)
        l_space = l_space - new_length
        return line, l_space
    
    @staticmethod   
    def add_spaces(line, l_spaces):
        '''
        adds l_spaces in front of line
        '''

        spaces = " " * l_spaces
        return spaces + line
    
    @staticmethod
    def translate(line):
        '''
        skeleton
        '''
        return line

parser = argparse.ArgumentParser(description='Animates python code.')
parser.add_argument('filename', type=str, help='the file to animate')
args = parser.parse_args()

file = File(args.filename)
file.run()
