from sly import Parser
from lexer import NLPLLexer
from stack import Stack

stack = Stack()
fenv = {}
log = open("parser.log", "w+")


class Statement:
    def __init__(self, type):
        self.type = type


class Definition:
    def __init__(self, name, body):
        self.name = name,
        self.body = body


class NLPLParser(Parser):
    # Uncomment this line to enable syntax debugging
    debugfile = "parser.out"

    # Get the token list from the lexer (required)
    tokens = NLPLLexer.tokens

    '''Grammar rules and actions'''
    @_("definition_list statement_list")
    def program(self, p):
        print("program")
        return p.statement_list, p.definition_list


    # Function definitions
    @_("definition definition_list")
    def definition_list(self, p):
        print("definition")
        return p.definition, p.definition_list

    @_("empty")
    def definition_list(self, p):
        print("list")
        pass

    @_("BEGIN_DEF statement END_DEF")
    def definition(self, p):
        print("definition " + p.BEGIN_DEF)
        fenv[p.BEGIN_DEF] = p.statement


    # Statements
    @_("statement statement_list")
    def statement_list(self, p):
        return p.statement, p.statement_list

    @_("empty")
    def statement_list(self, p):
        pass


    # Stack manipulation
    @_("PUSH")
    def statement(self, p):
        stack.push(len(p.PUSH))
        return p.statement

    @_("POP")
    def statement(self, p):
        stack.pop()
        return p.statement

    @_("SWAP")
    def statement(self, p):
        stack.swap()
        return p.statement


    # Operators
    @_("ADD")
    def statement(self, p):
        stack.push(stack.pop() + stack.pop())
        return p.statement

    @_("SUB")
    def statement(self, p):
        top1 = stack.pop()
        top2 = stack.pop()
        stack.push(top2 - top1)
        return p.statement

    @_("MUL")
    def statement(self, p):
        print("mul")
        stack.push(stack.pop() * stack.pop())
        return p.statement

    @_("DIV")
    def statement(self, p):
        top1 = stack.pop()
        top2 = stack.pop()
        stack.push(top2 / top1)
        return p.statement

    @_("CALL")
    def statement(self, p):
        return fenv[p.CALL], p.statement


    # IO
    @_("PRINT")
    def statement(self, p):
        print("Print")
        print(chr(round(stack.top())), end="")
        return p.statement

    # Misc
    @_("ENDL")
    def statement(self, p):
        pass

    @_("")
    def empty(self, p):
        pass

