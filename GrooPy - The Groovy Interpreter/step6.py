import sys
data=" "
#TOkens-->
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF'
)


#Token Class--> Has Type and Value Corresponding to It
class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        # returns a string in Token style
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

# Lexer Creates Tokens  Has 3 properties -> text to interpret, current pos and current char
class Lexer(object):
    def __init__(self, text):
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)


    #tokenizer creates token for current char and goes to next

    def get_next_token(self):

        while self.current_char is not None:

            #skip whitespaces
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            #if char is digit then get the whole no
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            #get operators

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            self.error()

        return Token(EOF, None)

#Interpreter class has properties lexer (tokens from lexer) and a current token
class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()


    # RULE 1-->
    def factor(self):
        """factor : INTEGER | LPAREN expr RPAREN"""
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)

            print('FACTOR:',token.value)
            return token.value
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()   #recursive call to expr again
            self.eat(RPAREN)

            print('FACTOR:',result)
            return result

    # RULE 2 -->
    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        result = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)

                print("MUL")
                result = result * self.factor()
            elif token.type == DIV:
                self.eat(DIV)

                print("DIV")
                result = result / self.factor()


        print('TERM:',result)
        return result

    # RULE 3 -->
    def expr(self):
        """
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER | LPAREN expr RPAREN
        """
        # first get the term
        result = self.term()

        # check for next if present
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                print('ADD')
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                print('SUB')
                result = result - self.term()

        print('EXPR:',result)
        return result


def main():
    mode= sys.argv[1]
    if mode=='1':
        print("-------------GrooPy------------\n")
        while True:
           try:
              text = input('::---> ')
           except EOFError:
               break
           if not text:
               continue
           lexer = Lexer(text)
           interpreter = Interpreter(lexer)
           result = interpreter.expr()
           print(result)

    elif mode=="2" :

        print('Debugger Mode')
        while True:
            try:
                text =input(':D:--->')
            except EOFError:
                break
            if not text:
                 continue
            lexer2= Lexer(text)
            lexer= Lexer(text)
            print("TOkens Created-->")
            print("--------------------")
            c= lexer.get_next_token()
            print(c)
            while c.type!=EOF:
                c=lexer.get_next_token()
                print(c)
            print("-------------------")
            print("TRAVERSAL:->")
            print('-------------------')
            int= Interpreter(lexer2)
            result=int.expr()
            print("-------------------")
            print("---:>",result)



    elif mode=='3' :

        file =sys.argv[2]
        file =open(file,'r')
        text= file.read().split('\n')

        for i in range(0,len(text)-1):
            lexer=Lexer(text[i])
            interpreter= Interpreter(lexer)
            result= interpreter.expr()
            print(result)



if __name__ == '__main__':
    main()