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