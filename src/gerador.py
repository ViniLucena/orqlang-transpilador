"""
Módulo: Gerador de código (tradução dirigida pela sintaxe / AST)
Objetivo: Transformar as estruturas sintáticas validadas pelo Parser em código Python executável.
Responsabilidades: 
- Mapear os comandos da OrqLang para comandos equivalentes em Python
- Traduzir SERVICO para chamadas de função, SE para if/else, REPITA para loops (for/while)
- Gerar o texto final do programa .py, garantindo a identação correta exigida pelo Python
"""