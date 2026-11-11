"""
Módulo: Gerador de código (tradução dirigida pela sintaxe / AST)
Objetivo: Transformar as estruturas sintáticas validadas pelo Parser em código Python executável
Responsabilidades: 
- Mapear os comandos da OrqLang para comandos equivalentes em Python
- Traduzir SERVICO para chamadas de função, SE para if/else, REPITA para loops (for/while)
- Gerar o texto final do programa .py, garantindo a identação correta exigida pelo Python
"""

def gerar_codigo(ast, nivel_identacao=0):
    """
    Percorre a AST de forma recursiva e gera o texto em Python
    O nível de identacão controla os blocos internos de ifs e loops
    """
    if ast is None:
        return ""
    
    # Define o espacamento atual (4 espacos por nível)
    prefixo = "    " * nivel_identacao
    codigo = ""
    
    # Se for uma lista, processa cada comando sequencialmente
    if isinstance(ast, list):
        for comando in ast:
            codigo += gerar_codigo(comando, nivel_identacao)
        return codigo
    
    # Se for uma tupla, processa de acordo com a etiqueta do nó
    if isinstance(ast, tuple):
        tipo_no = ast[0]
        
        if tipo_no == "programa":
            # ast = (programa, comandos)
            # Ignora a tag 'programa' e gera o código dos comandos internos
            codigo += gerar_codigo(ast[1], nivel_identacao)
            
        elif tipo_no == 'VAR':
            # ast = ('VAR', nome_variavel, expressao)
            expr_python = avaliar_expressao(ast[2])
            codigo += f"{prefixo}{ast[1]} = {expr_python}\n"
            
        elif tipo_no == 'IMPRIMIR':
            # ast = ('IMPRIMIR', expressao)
            expr_python = avaliar_expressao(ast[1])
            codigo += f"{prefixo}print({expr_python})\n"

        elif tipo_no == 'SERVICO':
            # ast = ('SERVICO', nome, argumentos, variavel_retorno)
            nome_servico = ast[1]
            
            # Converte a lista de argumentos da AST para uma string separada por vírgulas 
            args_traduzidos = [avaliar_expressao(arg) for arg in ast[2]]
            str_argumentos = ", ".join(args_traduzidos)
        
            if ast[3] is not None:
                codigo += f"{prefixo}{ast[3]} = {nome_servico}({str_argumentos})\n"
            else:
                codigo += f"{prefixo}{nome_servico}({str_argumentos})\n"
        
        elif tipo_no == 'SE':
            # ast = ('SE', condicao, comandos_entao, comandos_senao)
            condicao_python = avaliar_expressao(ast[1])
            codigo += f"{prefixo}if {condicao_python}:\n"
            codigo += gerar_codigo(ast[2], nivel_identacao + 1)
            
            if ast[3] is not None:
                codigo += f"{prefixo}else:\n"
                # Aumenta a identação para o bloco 'senao'
                codigo += gerar_codigo(ast[3], nivel_identacao+1)
                
        elif tipo_no == 'REPITA':
            # ast = ('REPITA', quantidade, comandos)
            qtd_python = avaliar_expressao(ast[1])
            # Garantindo que o valor é um int
            codigo += f"{prefixo}for _ in range({qtd_python}):\n"
            
            # Aumenta a identacao para o bloco do loop
            codigo += gerar_codigo(ast[2], nivel_identacao + 1)
            
    return codigo
            
        
            
def avaliar_expressao(expr):
    """
    Funcão pra traduzir expressões matemáticas, lógica e tipos primitivos (NUM, STR, VERDADEIRO e FALSO)
    """
    if not isinstance(expr, tuple):
        return str(expr)
    
    tipo = expr[0]
    
    match tipo:
        case 'NUM':
            return str(expr[1])
        case 'STR':
            return f'"{expr[1]}"'
        case 'ID':
            return expr[1]
        case 'VERDADEIRO':
            return "True"
        case 'FALSO':
            return "False"
        case 'NEG':
            return f"(-{avaliar_expressao(expr[1])})"
        case 'SOMA':  
            return f"({avaliar_expressao(expr[1])} + {avaliar_expressao(expr[2])})"
        case 'SUB':   
            return f"({avaliar_expressao(expr[1])} - {avaliar_expressao(expr[2])})"
        case 'MULT':  
            return f"({avaliar_expressao(expr[1])} * {avaliar_expressao(expr[2])})"
        case 'DIV':   
            return f"({avaliar_expressao(expr[1])} / {avaliar_expressao(expr[2])})"
        case 'IGUAL':    
            return f"({avaliar_expressao(expr[1])} == {avaliar_expressao(expr[2])})"
        case 'DIF':      
            return f"({avaliar_expressao(expr[1])} != {avaliar_expressao(expr[2])})"
        case 'MENOR':    
            return f"({avaliar_expressao(expr[1])} <  {avaliar_expressao(expr[2])})"
        case 'MAIOR':    
            return f"({avaliar_expressao(expr[1])} >  {avaliar_expressao(expr[2])})"
        case 'MENOR_IG': 
            return f"({avaliar_expressao(expr[1])} <= {avaliar_expressao(expr[2])})"
        case 'MAIOR_IG': 
            return f"({avaliar_expressao(expr[1])} >= {avaliar_expressao(expr[2])})"