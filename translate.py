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
    log_line = ""
    new_line = ""
    if re.compile('[+\-*/]=').search(line):
        line = remove_plus_eq(line)

    #if line.contains
    #if re.compile('\[.\].\[').search(line):
     #   print(line)
      #  log_line = modify_twoaccess(line)
       # print(log_line)

    if re.compile('=').search(line):
        return replace_assign(line)

    if re.compile('^for ').search(line):
        return modify_forloop(line)

    if re.compile('\.put').search(line):
        return  modify_queueput(line)

    if re.compile('\.get').search(line):
        return modify_queueget(line)

    if re.compile('\.append').search(line):
        return modify_listammend(line)


    return [line]
    #Other stuff

def modify_twoaccess(line):
    #print(line)
    line = line.split("append(")[1]
    splits = line.split("[")
    #print(splits)
    array_name = splits[0]
    index_one_var = splits[1].strip("]")
    index_two_var = splits[2].strip(")").strip("]")
    #print("name", array_name)
    #print("i1", index_one_var)
    #print("i2", index_two_var)
    log_line =  "self.logger.log(\"" + array_name + "\", str(type(" + array_name + ")) + \"-acc\" , None, (" + index_one_var + "," + index_two_var + "))"
    return log_line

def modify_queueput(line):
    vars = line.split('.')
    queue_name = vars[0]
    put_value = vars[1].split("(")[1].split(")")[0]
    #print(put_value)
    log_line = "self.logger.log(\"" + queue_name + "\", " \
            + "str(type(" + queue_name + ")) + \"-put\", " + put_value + ")"
    #print(log_line)
    return [line, log_line]

def modify_listammend(line):
    vars = line.split('.')
    list_name = vars[0]
    ammend_value = vars[1].split("(")[1].split(")")[0]
    #print(put_value)
    log_line = "self.logger.log(\"" + list_name + "\", " \
            + "str(type(" + list_name + ")), " + list_name + ", index=len(" + list_name + "))"
    #print(log_line):
    if line.count("[") == 2 and line.count("]") == 2:
        log_line += ";" + modify_twoaccess(line) + ";"
    return [line, log_line]

def modify_queueget(line):
    vars = line.split('.')
    queue_name = vars[0]
    log_line = "self.logger.log(\"" + queue_name + "\", " \
+ "str(type(" + queue_name + ")) + \"-get\", None)"
    #print(log_line)
    return [line, log_line]

def remove_plus_eq(line):
    vars = re.split("[+\-*/]=", line)
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


def modify_forloop(line):
    '''
    Append a logger for iterator variable of for-loop
    '''
    modified_forloop = [line]
    no_for_line = re.sub("for\W+", "", line)
    iterator_name = re.split("\W+in\W+", no_for_line)[0]
    modified_forloop.append("    self.logger.log(\"" + iterator_name + "\"" + ", str(type(" +
            iterator_name + ")), " + iterator_name + ");")
    return modified_forloop


def test_translate():
    print(translate("a = b"))
    print(translate("value = 5"))
    print(translate("p, q, r ,k,c= 1, 2, 'c', arg, getFunc()"))
    print(translate(" b = a + 1"))

if __name__ == "__main__":
    test_translate()
