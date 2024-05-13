from sly import Lexer


class NLPLLexer(Lexer):
    # Token names
    tokens = {
        # Function definition
        BEGIN_DEF,
        END_DEF,
        # Stack manipulation
        NUMBER,
        STRING,
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
        TO_CHAR,
        # Misc
        ENDL
    }

    # Literals
    literals = {}

    # Ignored characters
    ignore  = "\t"

    # Function definition
    BEGIN_DEF   = r" +A\s+[a-zA-Z]{2,}\s+dipped\s+in\s+Mama\s+Liz's\s+"
    END_DEF     = r"\s*oil"

    # Stack manipulation
    NUMBER      = r" *An?\s+[a-zA-Z]+"
    STRING      = r" *You\s+guys\s+[ever\s+]?hear\s+about\s+[a-zA-Z0-9]+"

    # Control flow
    BEGIN_WHILE = r" *Run\s+it\s+back"
    END_WHILE   = r" *I\s+got\s+one\s+more\s+in\s+me"
    BREAK       = r" *GET\s+ME\s+(OUTTA|OUT\s+OF)\s+HERE"
    TLZ         = r" *The\s+(reports|rumors)\s+(of|about)\s+my\s+(demise|death)\s+" \
                  r"have\s+been\s+greatly\s+exaggerated"
    TEQ         = r" *Him\s+me\s+him\s+him\s+me"
    BEGIN_IF    = r" *Nuts\s+on\s+the\s+table"
    END_IF      = r" *Nuts\s+off\s+the\s+table"

    # Functions/builtin calls
    CALL        = r" *[a-zA-Z]{2,}\s+me"

    # IO
    TO_CHAR     = r" *Write\s+that\s+down"
    PRINT       = r" *(Librarian\s*,\s+p|P)ull\s+that\s+(shit\s+)?up"

    # Misc
    ENDL        = r"\s*[\!\?\.]+[ \t]*"


    # Preprocess nodes
    def NUMBER(self, t):
        t.value = t.value.strip()[2:].replace(" ", "")
        return t

    def BEGIN_DEF(self, t):
        t.value = t.value[1:].strip().split(" ")[0]
        return t

    def CALL(self, t):
        t.value = t.value.strip().split(" ")[0]
        return t

    def STRING(self, t):
        t.value = t.value.split("about")[-1].strip()
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
