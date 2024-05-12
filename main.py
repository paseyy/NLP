from lexer import NLPLLexer
from parser import NLPLParser
import sys

if __name__ == "__main__":
    try:
        program_file = open(sys.argv[1], "r")
        program = program_file.read()
    except Exception:
        program = "A vagabond dipped in Mama Liz's Juice me oil???" \
                  "A hemomancer. A donkey. vagabond me." \
                  "Librarian, pull that up."

    lexer = NLPLLexer()
    parser = NLPLParser()

    try:
        tokens = lexer.tokenize(program)

        #for tok in tokens:
        #    print(tok)

        parser.parse(tokens)
    except EOFError:
        pass
    except Exception as e:
        print(e)
