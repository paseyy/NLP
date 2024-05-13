from parser import *
from stack import Stack


class BreakException(Exception):
    pass


class NLPLInterpreter:
    def __init__(self):
        self.stack = Stack()
        self.global_functions = {}


    def interpret(self, parseTree):
        function_definitions, program_body = parseTree

        self.interpretDefinitions(function_definitions)

        body = program_body.statements
        self.interpretBody(body)


    def interpretDefinitions(self, function_definitions: DefinitionList):
        functions = function_definitions.definitions

        for function in functions:
            self.global_functions[function.name[0]] = function.body


    def interpretBody(self, body):
        for statement in body:
            self.interpretStatement(statement)


    def interpretFunctionCall(self, statement: Call):
        match statement.name:
            case "Buy":
                self.stack.add()
            case "Sell":
                self.stack.sub()
            case "Juice":
                self.stack.mul()
            case "Squeeze":
                self.stack.div()
            case "Ice":
                self.stack.pop()
            case "Dup":
                self.stack.dup()
            case "Swap":
                self.stack.swap()
            case _:
                try:
                    self.interpretBody(self.global_functions[statement.name])
                except ValueError:
                    raise NameError("No function with this name: " + statement.name)


    def interpretStatement(self, statement):
        match statement.type:
            # Control flow
            case "WHILE":
                try:
                    while True:
                        self.interpretBody(statement.body)
                except BreakException:
                    pass

            case "BREAK":
                raise BreakException

            case "IF":
                if self.stack.pop():
                    self.interpretBody(statement.body)

            # Logic functions
            case "TLZ":
                self.stack.tlz()

            case "TEQ":
                self.stack.teq()

            # Stack manipulation
            case "NUMBER":
                self.stack.push(len(statement.value))
            case "STRING":
                self.stack.push(statement.value)

            # Function calls
            case "CALL":
                self.interpretFunctionCall(statement)

            # IO
            case "PRINT":
                print(self.stack.pop(), end="")
            case "TO_CHAR":
                self.stack.push(chr(round(self.stack.pop())))
