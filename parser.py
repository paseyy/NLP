from sly import Parser
from lexer import NLPLLexer


class Definition:
    def __init__(self, name, body):
        self.name = name,
        self.body = body


class DefinitionList:
    def __init__(self, definitions):
        self.definitions = definitions


class Statement:
    def __init__(self, type):
        self.type = type


class StatementList:
    def __init__(self, statements):
        self.statements = statements


class Call(Statement):
    def __init__(self, type, name):
        super().__init__(type),
        self.name = name


class Push(Statement):
    def __init__(self, type, value):
        super().__init__(type),
        self.value = value


class While(Statement):
    def __init__(self, type, body):
        super().__init__(type),
        self.body = body


class NLPLParser(Parser):
    # Uncomment this line to enable syntax debugging
    debugfile = "parser.out"

    # Get the token list from the lexer (required)
    tokens = NLPLLexer.tokens

    '''Grammar rules and actions'''
    @_("definition_list statement_list")
    def program(self, p):
        return DefinitionList(p[0]), StatementList(p[1])


    # Function definitions
    @_("definition definition_list")
    def definition_list(self, p):
        return [p.definition] + p.definition_list

    @_("empty")
    def definition_list(self, p):
        return []

    @_("BEGIN_DEF statement_list END_DEF")
    def definition(self, p):
        return Definition(p.BEGIN_DEF, p.statement_list)


    # Statements
    @_("statement statement_list")
    def statement_list(self, p):
        return [p.statement] + p.statement_list

    @_("empty")
    def statement_list(self, p):
        return []


    # Stack manipulation
    @_("PUSH")
    def statement(self, p):
        return Push("PUSH", p.PUSH)

    # Control flow
    @_("BEGIN_WHILE statement_list END_WHILE")
    def statement(self, p):
        return While("WHILE", p.statement_list)

    @_("BREAK")
    def statement(self, p):
        return Statement("BREAK")


    # Function/builtin calls
    @_("CALL")
    def statement(self, p):
        return Call("CALL", p.CALL)


    # IO
    @_("PRINT")
    def statement(self, p):
        return Statement("PRINT")


    # Misc
    @_("ENDL")
    def statement(self, p):
        pass


    # Empty rule
    @_("")
    def empty(self, p):
        pass

