#Method file for translating native python code
import re
from logger import Logger


def variable(self, variable, name):
    Logger.log(name, str(type(variable)), variable)


def translate(line):
    '''
    Translate all lines of code to be able to be logged
    @param line: string representing a line of code
    '''
    if re.compile('=').search(line):
        return replace_assign(line)

    #Other stuff


def replace_assign(line):
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
        assignment_li.append(left_obj[i] + " = "
                + "variable(" + left_obj[i] + "," + right_obj[i] + ")")

    return assignment_li

def test_translate():
    print(translate("a = b"))
    print(translate("value = 5"))
    print(translate("p, q, r ,k,c= 1, 2, 'c', arg, getFunc()"))
    print(translate(" b = a + 1"))

test_translate()
