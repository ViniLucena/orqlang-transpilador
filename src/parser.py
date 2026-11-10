"""
Módulo: Analisador Sintático (parser)
Objetivo: Receber a sequência de tokens do Lexer e validar se eles formam frases corretas segundo
as regras da Gramática Livre de Contexto (GLC) da OrqLang.
Responsabilidades: 
- Implementar as regras de derivação (EBNF convertida para regras do Yacc)
- Resolver precedência de operadores matemáticos e associatividade
- Validar aninhamento de blocos (SE/ENTAO/SENAO, REPITA)
- Acusar erros sintáticos (ex: esquecer de fechar um FIM ou parênteses)
Ferramenta: ply.yacc
"""

import ply.yacc as yacc
from lexer import tokens

def p_programa(p):
    'programa : INICIO comandos FIM'
    print("Programa válido!")
    p[0] = p[2]

def p_comandos_unico(p):
    'comandos : comando'
    p[0] = [p[1]]

def p_comandos_varios(p):
    'comandos : comandos comando'
    p[0] = p[1] + [p[2]]

def p_comando_var(p):
    'comando : VAR ID ATRIBUI expressao'
    p[0] = ('VAR', p[2], p[4])

def p_comando_imprimir(p):
    'comando : IMPRIMIR expressao'
    p[0] = ('IMPRIMIR', p[2])

def p_expressao_num(p):
    'expressao : NUM'
    p[0] = ('NUM', p[1])

def p_expressao_str(p):
    'expressao : STR'
    p[0] = ('STR', p[1])

def p_expressao_id(p):
    'expressao : ID'
    p[0] = ('ID', p[1])