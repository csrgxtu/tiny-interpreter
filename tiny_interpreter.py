# -*- coding: utf8 -*-
"""
A simple tiny interpreter that interpretes Py's byte code
"""

class TinyInterpreter(object):
    """
    TinyInterpreter will take simple byte code as input,
    and execute it
    """
    def __init__(self):
        self.stack = []
        self.environment = {}

    def STORE_NAME(self, name):
        """store name bind name and value
        
        Arguments:
            name {[string]} -- [description]
        """
        val = self.stack.pop()
        self.environment[name] = val
    
    def LOAD_NAME(self, name):
        """implementation of load name byte code
        
        Arguments:
            name {[string]} -- [name to load]
        """
        val = self.environment[name]
        self.stack.append(val)

    def LOAD_VALUE(self, number):
        """
        implementation of load value cmd
        :param number: int
        :return:
        """
        self.stack.append(number)

    def PRINT_ANSWER(self):
        """
        pop value out of stack and print it
        """
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        """
        pop two value from stack and added it
        """
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        self.stack.append(first_num + second_num)

    def parse_arg(self, instruction, arg, what_to_execute):
        """understand what arg means to each instruction
        
        Arguments:
            instruction {[str]} -- [description]
            arg {[str]} -- [description]
            what_to_execute {[dict]} -- [description]
        """
        numbers = ['LOAD_VALUE']
        names = ['LOAD_NAME', 'STORE_NAME']
        if instruction in numbers:
            arg = what_to_execute['numbers'][arg]
        elif instruction in names:
            arg = what_to_execute['names'][arg]
        return arg

    def run_code(self, what_to_execute):
        """
        loops each instruction, process args in each instruction,
        and calls corresponding method
        :param what_to_execute: dict
        :return:
        """
        instructions = what_to_execute.get('instructions', [])
        for each_instruct in instructions:
            instruction, arg = each_instruct
            arg = self.parse_arg(instruction, arg, what_to_execute)
            method = getattr(self, instruction)
            if arg is None:
                method()
            else:
                method(arg)

if __name__ == "__main__":
    # 1 + 2
    what_to_execute = {
        "instructions": [("LOAD_VALUE", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_VALUE", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [1, 2],
        "names":   ["a", "b"]
    }

    ti = TinyInterpreter()
    ti.run_code(what_to_execute)
