# ------------------------------------------------------------
# calcyacc.py
#   
#   Calc -> ...
# ------------------------------------------------------------
import sys
import ply.yacc as yacc
from calculadora_lex import tokens
from calculadora_lex import literals

varDic = dict({})
stackPos = 0
label = 0

'''
Instrucoes : Instrucoes Instrucao
           | Instrucao

Instrucao : Atr

Instrucao : if '(' Conds ')' '{ Instrucoes '}'

Conds: Conds && cond
Conds: Conds || cond
Conds: cond

Atr : id = Exp
    | id <<
    | >> id

Exp : Ramalho



'''

def p_Main(p):
    "Main : Instrucoes"
    p[0] = p[1]

def p_Instrucoes_Instrucoes(p):
    "Instrucoes : Instrucoes Instrucao"
    p[0] = p[1] + p[2]

def p_Instrucoes_Instrucao(p):
    "Instrucoes : Instrucao"
    p[0] = p[1]

def p_Instrucao_Atrib(p):
    "Instrucao : Atr"
    p[0] = p[1]

def p_Instrucao_Cond(p):
    "Instrucao : '?' '(' Conds ')' '{' Instrucoes '}'"
    global stackPos
    global label

    print(p[3])

    p[0] = "{0}\nJZ\nEND{1}\n{2}\nEND{1}:".format(p[3],label,p[6])
    label+=1

def p_Conds_Cond(p):
    "Conds : Cond"
    p[0] = p[1]
    

def p_Cond_less(p):
    "Cond : Exp '<' Exp"
    global stackPos
    p[0] = "{0}\n{1}\nINF".format(str(p[1]),str(p[3]))
    stackPos-=2

def p_Cond_more(p):
    "Cond : Exp '>' Exp"
    global stackPos
    p[0] = "{0}\n{1}\nSUP".format(str(p[1]),str(p[3]))
    stackPos-=2

def p_Cond_equals(p):
    "Cond : Exp '=' '=' Exp"
    global stackPos
    p[0] = "{0}\n{1}\nEQUAL".format(str(p[1]),str(p[4]))
    stackPos-=2

def p_Cond_less_equals(p):
    "Cond : Exp '<' '=' Exp"
    global stackPos
    p[0] = "{0}\n{1}\nINFEQ".format(str(p[1]),str(p[4]))
    stackPos-=2

def p_Cond_more_equals(p):
    "Cond : Exp '>' '=' Exp"
    global stackPos
    p[0] = "{0}\n{1}\nSUPEQ".format(str(p[1]),str(p[4]))
    stackPos-=2

def p_Cond_different(p):
    "Cond : Exp '!' '=' Exp"
    global stackPos
    p[0] = "{0}\n{1}\nEQUAL\nNOT".format(str(p[1]),str(p[4]))
    stackPos-=2



def p_Atr_id(p):
    "Atr : id '=' Exp"
    if p[1] not in varDic:
        global stackPos
        varDic[p[1]] = stackPos-1
        p[0] = str(p[3])
    else:
        pass

def p_Atr_print_str(p):
     "Atr : '$' string"
     global stackPos
     p[0] = "PUSHS {0}\n{1}".format(p[2],"WRITES")
     stackPos-=1

def p_Atr_print_int(p):
    "Atr : '$' int"
    global stackPos
    p[0] = "PUSHI {0}\n{1}".format(p[2],"WRITEI")
    stackPos-=1

def p_Atr_read(p):
     "Atr : '$'"
     global stackPos
     p[0] = "{0}\n{1}".format("READ","ATOI")
     stackPos+=1


def p_Exp_add(p):
    "Exp : Exp '+' Term"
    global stackPos
    p[0] = "{0}\n{1}\n{2}".format(p[1],p[3],"ADD")
    stackPos-=1

def p_Exp_sub(p):
    "Term : Term '-' Factor"
    global stackPos
    p[0] = "{0}\n{1}\n{2}".format(p[1],p[3],"SUB")
    stackPos-=1

def p_Exp_term(p):
    "Exp : Term"
    p[0] = p[1]

def p_Term_mul(p):
    "Term : Term '*' Factor"
    global stackPos
    p[0] = "{0}\n{1}\n{2}".format(p[1],p[3],"MUL")
    stackPos-=1

def p_Term_div(p):
    "Term : Term '/' Factor"
    global stackPos
    p[0] = "{0}\n{1}\n{2}".format(p[1],p[3],"DIV")
    stackPos-=1


def p_Term_factor(p):
    "Term : Factor"
    global stackPos
    p[0] = p[1]
    

def p_Factor_id(p):
    "Factor : id"
    global stackPos
    p[0] = "PUSHG {0}".format(varDic.get(str(p[1])))
    stackPos+=1

def p_Factor_int(p):
    "Factor : int"
    global stackPos
    p[0] = "PUSHI {0}".format(p[1])
    stackPos+=1
    

def p_Factor_float(p):
    "Factor : float"
    global stackPos
    p[0] = "PUSHF {0}".format(p[1])
    stackPos+=1

def p_Factor_string(p):
    "Factor : string"
    global stackPos
    p[0] = "PUSHS {0}".format(p[1])
    stackPos+=1


















#----------------------------------------
def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

#----------------------------------------
#inicio do Parser e Calculadora
parser = yacc.yacc()

parser.success = True
parser.registers = {}

for line in sys.stdin:
    print(parser.parse(line))
    
        



