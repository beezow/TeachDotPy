#Method file for translating native python code
import re
from logger import Logger


def variable(name, variable):
    Logger.log(name, str(type(variable)), variable)


def translate(line):
    '''
    Translate all lines of code to be able to be logged
    @param line: string representing a line of code
    '''


    if re.compile('+=').search(line):
        line = remove_plus_eq(line)
    if re.compile('=').search(line):
        return replace_assign(line)

    return [line]
    #Other stuff

def remove_plus_eq(line):
    vars = line.split("[+-*/]=")
    op_index = len(vars[0])
    new_line = vars[0] + "=" + vars[0] + line[op_index] + vars[1]
    return new_line

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
        assignment_li.append(line + "; self.logger.log(\"" + left_obj[i] + "\"" + ", str(type(" +
                left_obj[i] + ")), " + left_obj[i] + ")")

    return assignment_li

def test_translate():
    print(translate("a = b"))
    print(translate("value = 5"))
    print(translate("p, q, r ,k,c= 1, 2, 'c', arg, getFunc()"))
    print(translate(" b = a + 1"))

if __name__ == "__main__":
    test_translate()
