# Roteiro de Desenvolvimento

## Fase 1: Configuração Inicial e Ambiente

[x] Criar estrutura de diretórios (src/, exemplos/, testes/, etc.).

[x] Configurar o repositório Git e conectar ao GitHub.

[x] Criar arquivo .gitignore.

[x] Configurar o ambiente virtual Python (venv).

[x] Instalar a biblioteca PLY (pip install ply) e atualizar requirements.txt.

[x] Inserir comentários descritivos no cabeçalho dos arquivos base.

## Fase 2: Analisador Léxico (src/lexer.py)

[ ] Definir a tupla tokens com os nomes dos símbolos.

[ ] Mapear as palavras reservadas (INICIO, FIM, VAR, SERVICO, IMPRIMIR, VERDADEIRO, FALSO, SE, ENTAO, SENAO, REPITA, VEZES).

[ ] Escrever RegEx para identificadores (ID).

[ ] Escrever RegEx para números inteiros e decimais (NUM).

[ ] Escrever RegEx para strings entre aspas duplas (STR).

[ ] Implementar regra para ignorar espaços, tabulações e quebras de linha (atualizando o contador de linhas).

[ ] Implementar regra para ignorar comentários (iniciados por #).

[ ] Implementar a função de tratamento de erros léxicos (t_error).

[ ] Teste: Rodar o Lexer isoladamente imprimindo os tokens do exemplos/01_basico.orq.

## Fase 3: Analisador Sintático Base (src/parser.py)

[ ] Configurar a importação dos tokens gerados pelo Lexer.

[ ] Implementar a regra raiz do programa (programa : INICIO comandos FIM).

[ ] Implementar o encadeamento de comandos (comandos : comando | comandos comando).

[ ] Regra de atribuição: VAR ID = expr.

[ ] Regra de impressão: IMPRIMIR expr.

[ ] Regra de chamada de serviço sem retorno: SERVICO ID ( argumentos ).

[ ] Regra de chamada de serviço com retorno: SERVICO ID ( argumentos ) -> ID.

[ ] Função de tratamento de erros sintáticos (p_error) indicando a linha do erro.

## Fase 4: Extensões Obrigatórias (Sintaxe e Precedência)

[ ] Expressões Aritméticas: Adicionar regras para +, -, *, /.

[ ] Precedência: Configurar a tupla precedence no PLY para resolver ambiguidades matematicas e associatividade à esquerda.

[ ] Adicionar suporte a parênteses nas expressões: ( expr ).

[ ] Adicionar suporte ao sinal unário negativo (-5, -x).

[ ] Operadores de Comparação: ==, !=, <, <=, >, >=.

[ ] Condicionais: Implementar SE expr ENTAO comandos FIM e SE expr ENTAO comandos SENAO comandos FIM. (Atenção à ambiguidade do dangling-else!)

[ ] Repetição: Implementar REPITA expr VEZES comandos FIM.

## Fase 5: Geração de Código (src/gerador.py e src/main.py)

Dica: Esta fase pode ser feita em paralelo com as fases 3 e 4, adicionando ações semânticas diretamente nas regras do parser.

[ ] Criar o script main.py para ler um arquivo .orq, invocar o parser e salvar o .py.

[ ] Injetar from runtime.servicos import * no topo do código gerado.

[ ] Traduzir VAR para atribuições simples no Python.

[ ] Traduzir IMPRIMIR para print().

[ ] Traduzir comandos SERVICO para chamadas de função Python.

[ ] Traduzir blocos SE/SENAO para if/else (garantindo a indentação correta gerada no texto final).

[ ] Traduzir bloco REPITA para um loop for _ in range(...) no Python.

## Fase 6: Bônus - Paralelismo (Opcional)

[ ] Adicionar a palavra reservada PARALELO no Lexer.

[ ] Criar a regra sintática para PARALELO chamadas FIM.

[ ] Validar estruturalmente que dentro do bloco só ocorram atribuições de serviços com variáveis distintas.

[ ] Traduzir o bloco para utilizar o executar_paralelo do arquivo runtime/orqlang_runtime.py.

## Fase 7: Testes e Validação

[ ] Executar o transpilador sobre todos os arquivos .orq do kit.

[ ] Rodar os arquivos .py gerados e comparar com os .esperado.txt.

[ ] Criar no mínimo mais 5 programas testes próprios (incluindo ao menos 1 com erro).

[ ] Validar se o compilador rejeita corretamente os casos em invalidos.orq.txt com mensagens úteis.

## Fase 8: Fechamento e Entrega

[ ] Escrever o relatório (formato PDF ou MarkDown exportado):

[ ] Nomes e matrículas.

[ ] Gramática final (pode ser a lista de regras EBNF ou do formato Yacc).

[ ] Decisões de projeto/tradução adotadas.

[ ] Instruções de como rodar o projeto.

[ ] Limitações encontradas.

[ ] Revisar pastas para não incluir __pycache__, venv ou arquivos .pyc.

[ ] Gerar o arquivo ZIP final e submeter no EAD.