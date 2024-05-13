from sly import Lexer


class NLPLLexer(Lexer):
    # Token names
    tokens = {
        # Function definition
        BEGIN_DEF,
        END_DEF,
        # Stack manipulation
        PUSH,
        # Control flow
        BEGIN_WHILE,
        END_WHILE,
        BREAK,
        TLZ,
        TEQ,
        BEGIN_IF,
        END_IF,
        # Function/builtin calls
        # handled as builtin functions: ADD, SUB, MUL, DIV, POP, DUP, SWAP
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
    BEGIN_DEF   = r"\*+A\s+[a-zA-Z]{2,}\s+dipped\s+in\s+Mama\s+Liz's\s+"
    END_DEF     = r"\s*oil\s*\?+"

    # Stack manipulation
    PUSH    = r"\s*An?\s+[a-zA-Z]+"

    # Control flow
    BEGIN_WHILE = r"\s*Run\s+it\s+back"
    END_WHILE   = r"\s*I\s+got\s+one\s+more\s+in\s+me"
    BREAK       = r"\s*GET\s+ME\s+(OUTTA|OUT\s+OF)\s+HERE\s*(\!+)?"
    TLZ         = r"\s*The\s+(reports\s+of|rumors\s+about)\s+my\s+(demise|death)\s+" \
                  r"have\s+been\s+greatly\s+exaggerated"
    TEQ         = r"\s*Him\s+me\s+him\s+him\s+me"
    BEGIN_IF    = r"\s*Nuts\s+on\s+the\s+table"
    END_IF      = r"\s*Nuts\s+off\s+the\s+table"
    # Functions/builtin calls
    CALL    = r"\s*[a-zA-Z]{2,}\s+me"

    # IO
    PRINT   = r"\s*(Librarian\s*,\s+pull\s+that\s+(shit\s+)?up)|(Pull\s+that\s+shit\s+up)"

    # Misc
    ENDL    = r"\s*\.[ \t]*"


    # Preprocess nodes
    def PUSH(self, t):
        t.value = t.value[2:].strip().replace(" ", "")
        return t

    def BEGIN_DEF(self, t):
        t.value = t.value[1:].strip().split(" ")[0]
        return t

    def CALL(self, t):
        t.value = t.value.strip().split(" ")[0]
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
