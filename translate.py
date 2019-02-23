#Method file for translating native python code
import re
from logger import Logger


def variable(self, variable, name):
    Logger.log(name, str(type(variable)), variable)


def translate(line):
    '''
    Replace line containing assignment operator with an assignment object
    @param line: string representing a line of code
    '''
    split_line = line.split("=")
    left = split_line[0]
    right = split_line[1]

    assignment_li = []
    left_obj = left.split(",")
    right_obj = right.split(",")

    for i in range(len(left_obj)):
        left_obj[i] = left_obj[i].strip()
        right_obj[i] = right_obj[i].strip()
        assignment_li.append(left_obj[i] + " = " + "Variable(" + right_obj[i] + ")")

    return assignment_li

def test_translate():
    print(translate("a = b"))
    print(translate("value = 5"))
    print(translate("p, q, r ,k,c= 1, 2, 'c', arg, getFunc()"))

test_translate()
