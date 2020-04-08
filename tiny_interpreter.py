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

    def run_code(self, what_to_execute):
        """
        loops each instruction, process args in each instruction,
        and calls corresponding method
        :param what_to_execute: dict
        :return:
        """
        instructions = what_to_execute.get('instructions', [])
        numbers = what_to_execute.get('numbers', [])
        for each_instruct in instructions:
            instruction, arg = each_instruct
            if instruction == 'LOAD_VALUE':
                number = numbers[arg]
                self.LOAD_VALUE(number)
            elif instruction == 'ADD_TWO_VALUES':
                self.ADD_TWO_VALUES()
            else:  # PRINT_ANSWER
                self.PRINT_ANSWER()


if __name__ == "__main__":
    # 7 + 5
    what_to_execute = {
        'instructions': [
            ('LOAD_VALUE', 0),
            ('LOAD_VALUE', 1),
            ('ADD_TWO_VALUES', None),
            ('PRINT_ANSWER', None)
        ],
        'numbers': [7, 5]
    }

    ti = TinyInterpreter()
    ti.run_code(what_to_execute)
