from sly import Lexer


class NLPLLexer(Lexer):
    # Token names
    tokens = {
        # Function definition
        BEGIN_DEF,
        END_DEF,
        # Stack manipulation
        PUSH,
        POP,
        SWAP,
        # Operators
        ADD,
        SUB,
        MUL,
        DIV,
        CALL,
        # IO
        PRINT,
        # Misc
        ENDL
    }

    # Literals
    literals = {}

    # Ignored characters
    ignore  = "\t"

    # Function definition
    BEGIN_DEF   = r"A\s+[a-zA-Z]{2,}\s+dipped\s+in\s+Mama\s+Liz's\s+"
    END_DEF     = r"\s*oil\s*\?+"

    # Stack manipulation
    PUSH    = r"An?\s+[a-zA-Z]{2,}"
    POP     = r"Ice\s+me."
    SWAP    = r"Swap\s+me"

    # Operators
    ADD     = r"Buy\s+me"
    SUB     = r"Sell\s+me"
    MUL     = r"Juice\s+me"
    DIV     = r"Squeeze\s+me"
    CALL    = r"[a-zA-Z]{2,}\s+me"

    # IO
    PRINT   = r"(Librarian\s*,\s+pull\s+that\s+(shit\s+)?up)|(Pull\s+that\s+shit\s+up)"

    # Misc
    ENDL    = r"\s*\.[ \t]*"


    # Preprocess nodes
    def PUSH(self, t):
        t.value = t.value[2:].replace(" ", "")
        return t

    def BEGIN_DEF(self, t):
        t.value = t.value[1:].strip().split(" ")[0]
        return t

    def CALL(self, t):
        t.value = t.value.split(" ")[0]
        return t

    # remove statement separators
    def ENDL(self, t):
        pass

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Invalid statement \"%s\".' % (self.lineno, t.value.split(".")[0]))
        self.index += len(t.value.split(".")[0])
