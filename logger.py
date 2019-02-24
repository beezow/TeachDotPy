import json
import re
import queue
class Logger(object):
    '''
    Records states of various objects and exports that to a json file
    '''

    def __init__(self):
        self.logbook = {}
        self.logbook['steps'] = []


    def log(self, name, typ, data, index=None):
        '''
        Takes in a turn and adds that to the currentTurn list.
        @param name: the variable name to log state as.
        @param type: the data type of the variable
        @param data: the data stored in the variable
        '''
        state = {}
        state['name'] = name
        state['type'] = typ
        try:
            state['data'] = data.copy()
        except:
            if type(data) == type(queue.Queue()):
                state['data'] = list(data.queue)
            else:
                state['data'] = data

        state['index'] = index

        self.logbook['steps'].append(state)


    def to_json(self, output):
        '''
        Outputs logbook to a json file.
        @param output: file to output json to
        '''
        with open(output, 'w') as outfile:
            json.dump(self.logbook, outfile, indent=4)


    def list_index(self, var_name):
        '''
        Outputs the index from referencing list, if var_name is a list
        '''
        indices = re.findall("\[[^\[\]]\]", var_name)
        for i in range(len(indices)):
            indices[i] = re.sub("[\[\]]", "", indices[i])
        return indices


    #def __str__(self):
     #   return str(self.logbook)


def test_logger(output_file):
    logger = Logger()
    logger.log('var_a', 'list', '[a,b,c,d,e]')
    logger.log('var_b', 'int', '23')
    logger.log('var_b', 'stack', '[a,b,e,f,g]')

    logger.to_json(output_file)
if __name__ == "__main__":
    test_logger('test_json/test_json_log.txt')
