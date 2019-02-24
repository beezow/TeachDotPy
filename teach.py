#!/usr/bin/python3
import argparse
import os

from translate import *
from logger import Logger

class File:
    def __init__(self, inname, outname):
        self.translated = ""
        self.load_file(inname)
        self.logger = Logger()
        self.outname = outname

    def run(self):
        '''
        runs translated file
        '''
        print(self.translated)
        exec(self.translated)
        self.logger.to_json(self.outname)

    def load_file(self, filename):
        '''
        reads in file, translating line by line,
        storing back into self.file_strings
        '''

        with open(filename, "r") as file:
            for line in file:
                if len(line.strip()) == 0: continue
                new_line, l_space = File.strip_spaces(line)
                new_line = new_line.strip()
                trans_lines = translate(new_line)
                if not trans_lines: continue
                for trans in trans_lines:
                    trans = File.add_spaces(trans, l_space)
                    self.translated += trans + "\n"

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


parser = argparse.ArgumentParser(description='Animates python code.')
parser.add_argument('infile', type=str, help='the file to animate')
parser.add_argument('logfile', type=str, default='log/teach.json', help='the file to save the animation json info')
args = parser.parse_args()

file = File(args.infile, args.logfile)
file.run()
os.system("java -jar processing-py.jar animation_maker/animation_maker/animation_maker.pyde")
