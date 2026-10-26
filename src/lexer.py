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