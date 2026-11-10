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


precedence = (
    ('nonassoc', 'IGUAL', 'DIF', 'MENOR', 'MENOR_IG', 'MAIOR', 'MAIOR_IG'),
    ('left', 'SOMA', 'SUB'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMENOS'),
)

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

def p_comando_servico_sem_retorno(p):
    'comando : SERVICO ID APARENT argumentos FPARENT'
    p[0] = ('SERVICO', p[2], p[4], None)

def p_comando_servico_com_retorno(p):
    'comando : SERVICO ID APARENT argumentos FPARENT SETA ID'
    p[0] = ('SERVICO', p[2], p[4], p[7])

def p_argumentos_vazio(p):
    'argumentos : '
    p[0] = []

def p_argumentos_lista(p):
    'argumentos : lista_argumentos'
    p[0] = p[1]

def p_lista_argumentos_um(p):
    'lista_argumentos : expressao'
    p[0] = [p[1]]

def p_lista_argumentos_varios(p):
    'lista_argumentos : lista_argumentos VIRGULA expressao'
    p[0] = p[1] + [p[3]]

def p_comando_se(p):
    'comando : SE expressao ENTAO comandos FIM'
    p[0] = ('SE', p[2], p[4], None)

def p_comando_se_senao(p):
    'comando : SE expressao ENTAO comandos SENAO comandos FIM'
    p[0] = ('SE', p[2], p[4], p[6])

def p_comando_repita(p):
    'comando : REPITA expressao VEZES comandos FIM'
    p[0] = ('REPITA', p[2], p[4])

def p_expressao_parenteses(p):
    'expressao : APARENT expressao FPARENT'
    p[0] = p[2]

def p_expressao_negativa(p):
    'expressao : SUB expressao %prec UMENOS'
    p[0] = ("NEG", p[2])

def p_expressao_igual(p):
    'expressao : expressao IGUAL expressao'
    p[0] = ("IGUAL", p[1], p[3])

def p_expressao_dif(p):
    'expressao : expressao DIF expressao'
    p[0] = ("DIF", p[1], p[3])

def p_expressao_menor(p):
    'expressao : expressao MENOR expressao'
    p[0] = ("MENOR", p[1], p[3])

def p_expressao_maior(p):
    'expressao : expressao MAIOR expressao'
    p[0] = ("MAIOR", p[1], p[3])

def p_expressao_menor_igual(p):
    'expressao : expressao MENOR_IG expressao'
    p[0] = ("MENOR_IG", p[1], p[3])

def p_expressao_maior_igual(p):
    'expressao : expressao MAIOR_IG expressao'
    p[0] = ("MAIOR_IG", p[1], p[3])

def p_expressao_soma(p):
    'expressao : expressao SOMA expressao'
    p[0] = ("SOMA", p[1], p[3])

def p_expressao_sub(p):
    'expressao : expressao SUB expressao'
    p[0] = ("SUB", p[1], p[3])

def p_expressao_mult(p):
    'expressao : expressao MULT expressao'
    p[0] = ("MULT", p[1], p[3])

def p_expressao_div(p):
    'expressao : expressao DIV expressao'
    p[0] = ("DIV", p[1], p[3])

def p_expressao_num(p):
    'expressao : NUM'
    p[0] = ('NUM', p[1])

def p_expressao_str(p):
    'expressao : STR'
    p[0] = ('STR', p[1])

def p_expressao_id(p):
    'expressao : ID'
    p[0] = ('ID', p[1])

def p_expressao_verdadeiro(p):
    'expressao : VERDADEIRO'
    p[0] = ('VERDADEIRO',)

def p_expressao_falso(p):
    'expressao : FALSO'
    p[0] = ('FALSO',)

def p_error(p):
    if p:
        print(f"ERRO SINTATICO: token inesperado '{p.value}' na linha {p.lineno}")
    else:
        print("ERRO SINTATICO: fim de arquivo inesperado (faltou um FIM?)")

parser = yacc.yacc()