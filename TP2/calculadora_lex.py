import ply.lex as lex
import sys

# List of token names.   This is always required
tokens = (
    'int', 'id','float', 'string', 'and', 'or','if'
)
# Literals
literals = ['+', '-', '*', '/', '(', ')', '?', '!','<','>','[',']',',','{','}','=','$']

# A regular expression rule with some action code
def t_float(t):
    r'\d+\.\d+'
    t.value = float(t.value)    
    return t

def t_and(t):
    r'and'    
    return t.value

def t_if(t):
    r'if'    
    return t.value

def t_or(t):
    r'or'    
    return t.value

# A regular expression rule with some action code
def t_int(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_string(t):
    r'"[\w ]{2,}"'
    t.value = t.value[1:-1] 
    return t

def t_id(t):
    r'[a-z]'
    return t
 
#----------------------------------------
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#----------------------------------------
# Build the lexer
lexer = lex.lex()
 
