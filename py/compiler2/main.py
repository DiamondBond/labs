from lexer import Lexer

def main:
    filename = 'lmao.ayy'
    file = open(filename, 'r')
    Lexer = Lexer(file)

    lexer.tokenizer()
    print "Tokens: "
    print lexer.tokens, "\n"

if __name__ = "__main__":
    main()
