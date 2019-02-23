import json

class Logger(object):
    '''
    Records states of various objects and exports that to a json file
    '''

    def __init__(self):
        self.logbook = {}
        self.logbook['steps'] = []
        self.currentTurn = []

    def log(self, name, type, data):
        '''
        Takes in a turn and adds that to the currentTurn list.
        @param name: the variable name to log state as.
        @param type: the data type of the variable
        @param data: the data stored in the variable
        '''
        state = {}
        state['name'] = name
        state['type'] = type 
        state['data'] = data

        self.currentTurn.append(state)

    def next_turn(self):
        '''
        Increments the turn to the next time interval
        '''
        turn_dict = {}
        turn_dict['objects'] = self.currentTurn
        self.logbook['steps'].append(turn_dict)
        self.currentTurn = []

    def to_json(self, output):
        '''
        Outputs logbook to a json file.
        @param output: file to output json to
        '''
        if len(self.currentTurn) != 0:
            next_turn()
        with open(output, 'w') as outfile:
            json.dump(self.logbook, outfile, indent=4)

    def __str__(self):
        return str(self.logbook)
    

def test_logger(output_file):
    logger = Logger()
    logger.log('var_a', 'list', '[a,b,c,d,e]')
    logger.log('var_b', 'int', '23')
    logger.next_turn()
    logger.log('var_b', 'stack', '[a,b,e,f,g]')

    logger.to_json(output_file)

