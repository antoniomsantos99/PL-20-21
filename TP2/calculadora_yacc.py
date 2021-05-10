# ------------------------------------------------------------
# calcyacc.py
#   
#   Calc -> ...
# ------------------------------------------------------------
import sys
import ply.yacc as yacc
from calculadora_lex import tokens

def p_Commands_list(p): 
    "Commands : Commands Command"
    pass

def p_Commands_com(p):
    "Commands : Command"
    pass

def p_Command_atrib(p):
    "Command : Atrib"
    pass

def p_Command_dump(p):
    "Command : DUMP"
    print("Registers: ", p.parser.registers)

def p_Command_print(p):
    "Command : '!' id"
    print(p.parser.registers.get(p[2]))
    
def p_Command_read(p):
    "Command : '?' id"
    valor = input("Introduza um valor inteiro: ")
    p.parser.registers.update({p[2] : int(valor)})
    print(f"Adicionado registo: {p[2]} = {valor}")

def p_Atrib(p):
    "Atrib : id ATR Exp"
    p.parser.registers.update({p[1] : p[3]})
    print

def p_Exp_add(p):
    "Exp : Exp '+' Term"
    print("ADD".format(p[3]))

def p_Exp_sub(p):
    p[0] = p[1] - p[3]

def p_Exp_term(p):
    "Exp : Term"

def p_Term_mul(p):
    "Term : Term '*' Factor"
    print("MUL".format(p[3]))

def p_Term_div(p):
    "Term : Term '/' Factor"
    print("DIV".format(p[3]))

def p_Term_factor(p):
    "Term : Factor"
    p[0] = p[1]
    

def p_Factor_id(p):
    "Factor : id"
    p[0] = p.parser.registers.get(p[1])

def p_Factor_number(p):
    "Factor : number"
    p[0] = p[1]
    print("PUSHI {0}".format(p[1]))

def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]

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
    parser.parse(line)
        
        



