
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "and array else float id if int or repeat string untilMain : InstrucoesInstrucoes : Instrucoes InstrucaoInstrucoes : InstrucaoInstrucao : AtrInstrucao : repeat '{' Instrucoes '}' until '(' Conditions ')'Instrucao : if '(' Conditions ')' '{' Instrucoes '}'Instrucao : if '(' Conditions ')' '{' Instrucoes '}' else '{' Instrucoes '}'Conditions : CondConditions : Conditions or CondCondition : Exp '<' ExpCondition : Exp '>' ExpCondition : Exp '=' '=' ExpCondition : Exp '<' '=' ExpCondition : Exp '>' '=' ExpCondition : Exp '!' '=' ExpCond : Cond and Cond2Cond : Cond2Cond2 : '!' CondCond2 : ConditionCond2 : '(' Conditions ')' Atr : id '=' ExpAtr : array '(' id ',' int ')'Atr : id '[' int ']' '=' ExpAtr : id '[' id ']' '=' ExpAtr : '$' stringAtr : '$' intAtr : '$'Exp : Exp '+' TermTerm : Term '-' FactorExp : TermTerm : Term '*' FactorTerm : Term '/' FactorTerm : FactorFactor : idFactor : intFactor : floatFactor : string"
    
_lr_action_items = {'repeat':([0,2,3,4,9,10,11,16,17,18,26,27,28,29,30,31,32,55,64,65,66,67,72,77,78,79,81,82,84,85,86,],[5,5,-3,-4,-27,-2,5,-25,-26,5,-30,-33,-34,-35,-36,-37,-21,5,-28,-29,-31,-32,5,-24,-23,-22,-6,-5,5,5,-7,]),'if':([0,2,3,4,9,10,11,16,17,18,26,27,28,29,30,31,32,55,64,65,66,67,72,77,78,79,81,82,84,85,86,],[6,6,-3,-4,-27,-2,6,-25,-26,6,-30,-33,-34,-35,-36,-37,-21,6,-28,-29,-31,-32,6,-24,-23,-22,-6,-5,6,6,-7,]),'id':([0,2,3,4,9,10,11,12,13,14,15,16,17,18,19,23,26,27,28,29,30,31,32,39,40,42,43,46,47,48,49,55,59,61,62,63,64,65,66,67,68,69,71,72,77,78,79,81,82,84,85,86,],[7,7,-3,-4,-27,-2,7,28,28,33,35,-25,-26,7,28,28,-30,-33,-34,-35,-36,-37,-21,28,28,28,28,28,28,28,28,7,28,28,28,28,-28,-29,-31,-32,28,28,28,7,-24,-23,-22,-6,-5,7,7,-7,]),'array':([0,2,3,4,9,10,11,16,17,18,26,27,28,29,30,31,32,55,64,65,66,67,72,77,78,79,81,82,84,85,86,],[8,8,-3,-4,-27,-2,8,-25,-26,8,-30,-33,-34,-35,-36,-37,-21,8,-28,-29,-31,-32,8,-24,-23,-22,-6,-5,8,8,-7,]),'$':([0,2,3,4,9,10,11,16,17,18,26,27,28,29,30,31,32,55,64,65,66,67,72,77,78,79,81,82,84,85,86,],[9,9,-3,-4,-27,-2,9,-25,-26,9,-30,-33,-34,-35,-36,-37,-21,9,-28,-29,-31,-32,9,-24,-23,-22,-6,-5,9,9,-7,]),'$end':([1,2,3,4,9,10,16,17,26,27,28,29,30,31,32,64,65,66,67,77,78,79,81,82,86,],[0,-1,-3,-4,-27,-2,-25,-26,-30,-33,-34,-35,-36,-37,-21,-28,-29,-31,-32,-24,-23,-22,-6,-5,-7,]),'}':([3,4,9,10,16,17,18,26,27,28,29,30,31,32,64,65,66,67,72,77,78,79,81,82,85,86,],[-3,-4,-27,-2,-25,-26,36,-30,-33,-34,-35,-36,-37,-21,-28,-29,-31,-32,81,-24,-23,-22,-6,-5,86,-7,]),'{':([5,38,83,],[11,55,84,]),'(':([6,8,12,19,23,39,40,53,71,],[12,15,19,19,19,19,19,71,19,]),'=':([7,25,26,27,28,29,30,31,42,43,44,45,50,51,64,65,66,67,],[13,44,-30,-33,-34,-35,-36,-37,59,61,62,63,68,69,-28,-29,-31,-32,]),'[':([7,],[14,]),'string':([9,12,13,19,23,39,40,42,43,46,47,48,49,59,61,62,63,68,69,71,],[16,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'int':([9,12,13,14,19,23,39,40,42,43,46,47,48,49,52,59,61,62,63,68,69,71,],[17,29,29,34,29,29,29,29,29,29,29,29,29,29,70,29,29,29,29,29,29,29,]),'!':([12,19,23,25,26,27,28,29,30,31,39,40,64,65,66,67,71,],[23,23,23,45,-30,-33,-34,-35,-36,-37,23,23,-28,-29,-31,-32,23,]),'float':([12,13,19,23,39,40,42,43,46,47,48,49,59,61,62,63,68,69,71,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),')':([20,21,22,24,26,27,28,29,30,31,37,41,54,56,57,58,60,64,65,66,67,70,73,74,75,76,80,],[38,-8,-17,-19,-30,-33,-34,-35,-36,-37,54,-18,-20,-9,-16,-10,-11,-28,-29,-31,-32,79,-13,-14,-12,-15,82,]),'or':([20,21,22,24,26,27,28,29,30,31,37,41,54,56,57,58,60,64,65,66,67,73,74,75,76,80,],[39,-8,-17,-19,-30,-33,-34,-35,-36,-37,39,-18,-20,-9,-16,-10,-11,-28,-29,-31,-32,-13,-14,-12,-15,39,]),'and':([21,22,24,26,27,28,29,30,31,41,54,56,57,58,60,64,65,66,67,73,74,75,76,],[40,-17,-19,-30,-33,-34,-35,-36,-37,40,-20,40,-16,-10,-11,-28,-29,-31,-32,-13,-14,-12,-15,]),'<':([25,26,27,28,29,30,31,64,65,66,67,],[42,-30,-33,-34,-35,-36,-37,-28,-29,-31,-32,]),'>':([25,26,27,28,29,30,31,64,65,66,67,],[43,-30,-33,-34,-35,-36,-37,-28,-29,-31,-32,]),'+':([25,26,27,28,29,30,31,32,58,60,64,65,66,67,73,74,75,76,77,78,],[46,-30,-33,-34,-35,-36,-37,46,46,46,-28,-29,-31,-32,46,46,46,46,46,46,]),'-':([26,27,28,29,30,31,64,65,66,67,],[47,-33,-34,-35,-36,-37,47,-29,-31,-32,]),'*':([26,27,28,29,30,31,64,65,66,67,],[48,-33,-34,-35,-36,-37,48,-29,-31,-32,]),'/':([26,27,28,29,30,31,64,65,66,67,],[49,-33,-34,-35,-36,-37,49,-29,-31,-32,]),']':([33,34,],[50,51,]),',':([35,],[52,]),'until':([36,],[53,]),'else':([81,],[83,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Main':([0,],[1,]),'Instrucoes':([0,11,55,84,],[2,18,72,85,]),'Instrucao':([0,2,11,18,55,72,84,85,],[3,10,3,10,3,10,3,10,]),'Atr':([0,2,11,18,55,72,84,85,],[4,4,4,4,4,4,4,4,]),'Conditions':([12,19,71,],[20,37,80,]),'Cond':([12,19,23,39,71,],[21,21,41,56,21,]),'Cond2':([12,19,23,39,40,71,],[22,22,22,22,57,22,]),'Condition':([12,19,23,39,40,71,],[24,24,24,24,24,24,]),'Exp':([12,13,19,23,39,40,42,43,59,61,62,63,68,69,71,],[25,32,25,25,25,25,58,60,73,74,75,76,77,78,25,]),'Term':([12,13,19,23,39,40,42,43,46,59,61,62,63,68,69,71,],[26,26,26,26,26,26,26,26,64,26,26,26,26,26,26,26,]),'Factor':([12,13,19,23,39,40,42,43,46,47,48,49,59,61,62,63,68,69,71,],[27,27,27,27,27,27,27,27,27,65,66,67,27,27,27,27,27,27,27,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Main","S'",1,None,None,None),
  ('Main -> Instrucoes','Main',1,'p_Main','calculadora_yacc.py',39),
  ('Instrucoes -> Instrucoes Instrucao','Instrucoes',2,'p_Instrucoes_Instrucoes','calculadora_yacc.py',43),
  ('Instrucoes -> Instrucao','Instrucoes',1,'p_Instrucoes_Instrucao','calculadora_yacc.py',47),
  ('Instrucao -> Atr','Instrucao',1,'p_Instrucao_Atrib','calculadora_yacc.py',51),
  ('Instrucao -> repeat { Instrucoes } until ( Conditions )','Instrucao',8,'p_Instrucao_loop','calculadora_yacc.py',55),
  ('Instrucao -> if ( Conditions ) { Instrucoes }','Instrucao',7,'p_Instrucao_Condition','calculadora_yacc.py',61),
  ('Instrucao -> if ( Conditions ) { Instrucoes } else { Instrucoes }','Instrucao',11,'p_Instrucao_Condition_else','calculadora_yacc.py',69),
  ('Conditions -> Cond','Conditions',1,'p_Conditions_Cond','calculadora_yacc.py',77),
  ('Conditions -> Conditions or Cond','Conditions',3,'p_Conditions_or_Cond','calculadora_yacc.py',81),
  ('Condition -> Exp < Exp','Condition',3,'p_Condition_less','calculadora_yacc.py',85),
  ('Condition -> Exp > Exp','Condition',3,'p_Condition_more','calculadora_yacc.py',91),
  ('Condition -> Exp = = Exp','Condition',4,'p_Condition_equals','calculadora_yacc.py',97),
  ('Condition -> Exp < = Exp','Condition',4,'p_Condition_less_equals','calculadora_yacc.py',103),
  ('Condition -> Exp > = Exp','Condition',4,'p_Condition_more_equals','calculadora_yacc.py',109),
  ('Condition -> Exp ! = Exp','Condition',4,'p_Condition_different','calculadora_yacc.py',115),
  ('Cond -> Cond and Cond2','Cond',3,'p_Cond_Cond_and','calculadora_yacc.py',121),
  ('Cond -> Cond2','Cond',1,'p_Cond_Cond2','calculadora_yacc.py',125),
  ('Cond2 -> ! Cond','Cond2',2,'p_Cond2_Not','calculadora_yacc.py',129),
  ('Cond2 -> Condition','Cond2',1,'p_Cond2_Condition','calculadora_yacc.py',133),
  ('Cond2 -> ( Conditions )','Cond2',3,'p_Cond2_Conditions','calculadora_yacc.py',137),
  ('Atr -> id = Exp','Atr',3,'p_Atr_id','calculadora_yacc.py',142),
  ('Atr -> array ( id , int )','Atr',6,'p_decl_Array','calculadora_yacc.py',149),
  ('Atr -> id [ int ] = Exp','Atr',6,'p_Atr_int_Array','calculadora_yacc.py',157),
  ('Atr -> id [ id ] = Exp','Atr',6,'p_Atr_id_Array','calculadora_yacc.py',165),
  ('Atr -> $ string','Atr',2,'p_Atr_print_str','calculadora_yacc.py',173),
  ('Atr -> $ int','Atr',2,'p_Atr_print_int','calculadora_yacc.py',179),
  ('Atr -> $','Atr',1,'p_Atr_read','calculadora_yacc.py',185),
  ('Exp -> Exp + Term','Exp',3,'p_Exp_add','calculadora_yacc.py',192),
  ('Term -> Term - Factor','Term',3,'p_Exp_sub','calculadora_yacc.py',198),
  ('Exp -> Term','Exp',1,'p_Exp_term','calculadora_yacc.py',204),
  ('Term -> Term * Factor','Term',3,'p_Term_mul','calculadora_yacc.py',208),
  ('Term -> Term / Factor','Term',3,'p_Term_div','calculadora_yacc.py',214),
  ('Term -> Factor','Term',1,'p_Term_factor','calculadora_yacc.py',221),
  ('Factor -> id','Factor',1,'p_Factor_id','calculadora_yacc.py',227),
  ('Factor -> int','Factor',1,'p_Factor_int','calculadora_yacc.py',233),
  ('Factor -> float','Factor',1,'p_Factor_float','calculadora_yacc.py',240),
  ('Factor -> string','Factor',1,'p_Factor_string','calculadora_yacc.py',246),
]
