from sys import *
def open_file(filename):
    data=open(filename,'r').read()
    return data+"<EOF>"



def lex(filecontents,tokens):
    filecontents=list(filecontents)


    state=0   #state 0-- Not inside a quote
              #state 1-- Inside a quote
    #state2=0  #state 0-- Not inside a single quote
              #state 1-- Inside a single quote
    tok=""
    var=""
    string=""
    isExpr=0
    expr=""
    n=""
    for char in filecontents:
        tok+=char     #cumulative

        #print(tok)

        #ignore spaces
        if tok==" ":
            if state==0:
                tok=""
            else :
                tok=" "
        elif tok=='\n' or tok=="<EOF>" or tok==";":
            if expr!="" and isExpr==1:
                #print(expr)
                #print("EXprs")
                tokens.append("EXP:"+expr)
                expr=""
            elif expr!="" and isExpr==0:
                #print(expr)
                #print("number")
                tokens.append("NUM:"+expr)
                expr=""
            tok=""

        #println statement
        elif tok=="println":
            #print("Found a Print")
            tokens.append("PRT")
            tok=""

        elif tok.isdigit():
            if state==0:
                expr+=tok
                tok=""

        elif tok=="+" or tok=="-" or tok=="/" or tok=="*" or tok=="**" :
            if state==0:
                isExpr=1
                expr+=tok
                tok=""


        #Double Quotes--  Identify if its start or end basedonstate
        elif tok=="\"":
            if state==0:
                state=1
                #start reading this string

            elif state==1:
                #end reading
                #print("Found a string:",string)
                tokens.append("STR:"+string+"\"")
                string=""
                state=0
                tok=""

        elif state==1:
            string+=tok
            #reset token
            tok=""

    #print(expr)
    #print(tokens)
    return tokens


def parse(toks):
    i=0
    while i<len(toks):

        if toks[i][:3]=="NUM" or toks[i][:3]=="EXP":
            print(eval(toks[i][4:]))
            i+=1
        elif toks[i][:3]=="STR":
            print(toks[i][5:-1])
            i+=1
        elif toks[i]+" "+toks[i+1][:3]=="PRT STR":
            print(toks[i+1][5:-1])
            i+=2
        elif toks[i]+" "+toks[i+1][:3]=="PRT NUM":
            print(toks[i+1][4:])
            i+=2
        elif toks[i]+" "+toks[i+1][:3]=="PRT EXP":
            print(eval(toks[i+1][4:]))
            i+=2



def run():
    mode=argv[1]
    if mode=='1':
        print('-----------------------------------------------------------------------------------')
        while True:
            data=str(input(':-->>'))
            if data=="EXIT":
               break
            else:
                cmd=[]
                data=data+"<EOF>"
                parse(lex(data,cmd))
                data=""


    elif mode=='0':
        data=open_file(argv[2])
        ls=[]
        parse(lex(data,ls))

    print()

run()

