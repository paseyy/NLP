from lexer import NLPLLexer
from parser import NLPLParser
from interpreter import NLPLInterpreter
import sys

if __name__ == "__main__":
    try:
        program_file = open(sys.argv[1], "r")
        program = program_file.read()
    except Exception:
        program = open("tests/loops.nlp", "r").read()

    lexer = NLPLLexer()
    parser = NLPLParser()
    interpreter = NLPLInterpreter()

    try:
        tokens = lexer.tokenize(program)

        # for tok in tokens:
        #     print(tok)

        parseTree = parser.parse(tokens)
        interpreter.interpret(parseTree)

    except EOFError:
        pass
    except Exception as e:
        print(e)
