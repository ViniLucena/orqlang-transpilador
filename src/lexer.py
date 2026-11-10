"""
Módulo: Analisador Léxico (lexer)
Objetivo: Ler o código-fonte (.orq) como uma string de texto e quebrar em uma sequência de
Tokens válidos da OrqLang (palavras reservadas, IDs, NUM, STR, etc).
Responsabilidades: 
- Definir os padrões de Expressões Regulares (Regex) para cada token
- Ignorar os espaços em branco e comentários (linhas que começam com #)
- Acusar e reportar erros léxicos (caracteres não reconhecidos)
Ferramenta: ply.lex
"""

import ply.lex as lex

# (roteiro): Definir a tupla tokens com o nome dos símbolos  
# A lista base deve conter os tokens literais e as categorias gerais (ID, NUM, STR)
# O PLY exige que a tupla se chame exatamente 'tokens'

tokens = (
    # Valores e identificadores
    'ID',
    'NUM',
    'STR',
    
    # Operadores aritméticos
    'SOMA',
    'SUB',
    'MULT',
    'DIV',
    
    # Operadores relacionais
    'IGUAL',
    'DIF',
    'MENOR',
    'MENOR_IG',
    'MAIOR',
    'MAIOR_IG',
    
    # Símbolos de estrutura
    'ATRIBUI',
    'SETA',
    'APARENT',
    'FPARENT',
    'VIRGULA',
)

# [x] Mapear as palavras reservadas.
# O uso de um dicionário é a melhor prática no PLY para evitar que identificadores 
# (como a variável "inicio_do_mes") sejam confundidos com a palavra reservada "INICIO".
palavras_reservadas = {
    'INICIO': 'INICIO',
    'FIM': 'FIM',
    'VAR': 'VAR',
    'SERVICO': 'SERVICO',
    'IMPRIMIR': 'IMPRIMIR',
    'VERDADEIRO': 'VERDADEIRO',
    'FALSO': 'FALSO',
    'SE': 'SE',
    'ENTAO': 'ENTAO',
    'SENAO': 'SENAO',
    'REPITA': 'REPITA',
    'VEZES': 'VEZES',
    'PARALELO': 'PARALELO' # Bônus opcional do roteiro
}

# Adicionamos as palavras reservadas dinamicamente à tupla de tokens
tokens = tokens + tuple(palavras_reservadas.values())

# --- Regras para Símbolos Simples (usando o prefixo t_ obrigatório do PLY) ---
# A ordem importa para operadores compostos vs simples (ex: == vs = e -> vs -)
t_SETA     = r'->'
t_IGUAL    = r'=='
t_DIF      = r'!='
t_MENOR_IG = r'<='
t_MAIOR_IG = r'>='

t_SOMA     = r'\+'
t_SUB      = r'-'
t_MULT     = r'\*'
t_DIV      = r'/'
t_MENOR    = r'<'
t_MAIOR    = r'>'
t_ATRIBUI  = r'='
t_APARENT  = r'\('
t_FPARENT  = r'\)'
t_VIRGULA  = r','

# [x] Escrever RegEx para strings entre aspas duplas (STR).
# O padrão captura as aspas no início/fim e qualquer coisa no meio, exceto quebras de linha ou novas aspas.
def t_STR(t):
    r'"[^\n]*"'
    # Removemos as aspas da string lida para facilitar o Parser depois
    t.value = t.value[1:-1]
    return t

# [x] Escrever RegEx para números inteiros e decimais (NUM).
# A regra lida com números float (ex: 2.5) e inteiros (ex: 10). 
# A parte decimal (\.\d+) é opcional (?).
def t_NUM(t):
    r'\d+(\.\d+)?'
    # Convertendo para float porque o python vai lidar com ambos no interpretador
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

# [x] Escrever RegEx para identificadores (ID) e checar palavras reservadas.
# Um ID começa com letra ou sublinhado, seguido por zero ou mais letras, números ou sublinhados.

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Consulta o dicionário. Se não achar, o tipo padrão é 'ID'
    t.type = palavras_reservadas.get(t.value, 'ID')
    return t

# [x] Implementar regra para ignorar espaços e tabulações.
# A string especial t_ignore é usada pelo PLY para pular os caracteres imediatamente.
t_ignore = '\t'

# [x] Implementar regra para ignorar comentários (iniciados por #).
# Essa função usa o padrão # seguido de qualquer caractere (.*) para varrer tudo. 
# O comentário não retorna token (pass) e assim é efetivamente ignorado pelo Lexer.
def t_comentario(t):
    r'\#.*'
    return None

# [x] Implementar regra para quebras de linha e atualização de contador.
# Isso é essencial para gerar mensagens de erro mostrando a linha exata.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# [x] Implementar a função de tratamento de erros léxicos.
# Atende a exigência de acusar erros e apontar linha/token quando possível
def t_error(t):
    print(f"ERRO LEXICO: Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    # Pula o caractere invalido para tentar continuar a analise
    t.lexer.skip(1)
    
# Compila e constrói a máquina de estados do analisador léxico
lexer = lex.lex()

# TESTE ISOLADO DO LEXER (SÓ EXECUTA SE O ARQUIVO FOR RODADO DIRETAMENTE)
if __name__ == "__main__":
    import sys
    import os
    
    # Determina o caminho para o arquivo 01_basico.orq
    # Assumindo que este script está rodando de orqlang-transpilador/src/
    caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho_arquivo = os.path.join(caminho_base, 'exemplos', '01_basico.orq')

    print(f"Testando o Lexer com o arquivo: {caminho_arquivo}\n")
    print("-" * 40)
    
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            codigo_fonte = arquivo.read()
            
        # Alimenta o lexer com o código lido
        lexer.input(codigo_fonte)
        
        # Itera sobre os tokens e imprime
        while True:
            tok = lexer.token()
            if not tok:
                break # Fim do arquivo atingido
            print(tok)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        print("Certifique-se de executar o comando a partir da pasta orqlang-transpilador.")