"""
Módulo: Ponto de entrada (CLI)
Objetivo: Orquestrar a execução do transpilador
Responsabilidades: 
- Receber o caminho do arquivo .orq passado pelo usuário via terminal
- Ler o conteúdo do arquivo
- Acionar o lexer e o parser/gerador para processar o texto
- Salvar o resultado final traduzido em um novo arquivo.py (na pasta gerado/) 
"""

import sys
import os

from parser import parser

from gerador import gerar_codigo

def compilar_arquivo(caminho_entrada):
    
    # Valida se a extensão do arquivo é .orq 
    if not caminho_entrada.endswith('.orq'):
        print("Erro! O arquivo de entrada tem que ser da extensao .orq")     
        return

    # Define o nome do arquivo de saída
    caminho_saida = caminho_entrada.replace('.orq', '.py')
    
    print(f"Iniciando transpilacao de {caminho_entrada}......")
    
    # Lendo o código-fonte da linguagem OrqLang
    try:
        with open(caminho_entrada, 'r', encoding='utf-8') as f:
            codigo_orq = f.read()
    except FileNotFoundError:
        print(f"Erro! Arquivo {caminho_entrada} nao encontrado")
        return
    
    # Análise sintática: lexer roda por baixo dos panos
    print("Construindo a arvore sintatica...")
    ast = parser.parse(codigo_orq)
    
    if ast is None:
        print("Falha na analise sintatica, transpilacao abortada")
        return
    
    print("Transpilacao concluida")
    
    # Geração de código Python (simulando a saída enquanto o gerador.py não é feito)
    print("Gerando codigo python...")
    
    # codigo_python = gerar_codigos(ast) # Descomentar quando fizer o gerador.py
    codigo_python_gerado = "# AQUI ENTRARÁ O CÓDIGO TRADUZIDO DA AST\n# print('Olá, Mundo!')\n"
    
    # Salva o arquivo final
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        # Injeta a importação obrigatória exigida pelo roteiro
        f.write("from runtime.servicos import *\n\n")
        
        # Escreve o código traduzido
        f.write(codigo_python_gerado)
        
    print(f"Arquivo gerado com sucesso em {caminho_saida}")
    
if __name__ == "__main__":
    # Permite rodar passando o arquivo via linha de comando
    # Exemplo: python src/main.py exemplos/01_basico.orq
    if len(sys.argv) > 1:
        arquivo_alvo = sys.argv[1]
    else:
    # Padrão de segurança para testes rápidos na IDE
        caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        arquivo_alvo = os.path.join(caminho_base, 'exemplos', '01_basico.orq')
    
    compilar_arquivo(arquivo_alvo)