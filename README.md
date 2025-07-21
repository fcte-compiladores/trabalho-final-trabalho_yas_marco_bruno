
# Interpretador Ook!

## Integrantes

- **Bruno Cunha Vasconcelos de Araujo** — 221034973 — [GitHub](https://github.com/brunocva)
- **Marco Túlio Soares** — 221008310 — [GitHub](https://github.com/MarcoTulioSoares)
- **Yasmin Kátia** — 200029088 — [GitHub](https://github.com/yaskisoba)

## Introdução

Este projeto consiste na implementação de um interpretador para a linguagem esotérica **Ook!**, uma variação do Brainfuck com comandos baseados em "Ook." e suas combinações. A linguagem foi escolhida pela sua estrutura minimalista, ideal para ilustrar os conceitos de tradução e execução de linguagens de baixo nível.

O interpretador realiza as seguintes etapas:

- **Análise léxica**: identifica os tokens `Ook. Ook?`, `Ook? Ook.`, etc., correspondentes às instruções de Brainfuck.
- **Tradução**: converte os comandos de Ook! em instruções Brainfuck equivalentes.
- **Execução**: interpreta e executa o código Brainfuck gerado.

A linguagem implementada possui 8 comandos, com a seguinte sintaxe e semântica:

| Comando Ook!         | Equivalente Brainfuck | Ação                                  |
|----------------------|-----------------------|----------------------------------------|
| `Ook. Ook?`          | `>`                   | Move o ponteiro para a direita         |
| `Ook? Ook.`          | `<`                   | Move o ponteiro para a esquerda        |
| `Ook. Ook.`          | `+`                   | Incrementa a célula atual              |
| `Ook! Ook!`          | `-`                   | Decrementa a célula atual              |
| `Ook! Ook.`          | `.`                   | Imprime o caractere na célula atual    |
| `Ook. Ook!`          | `,`                   | Lê um caractere para a célula atual    |
| `Ook! Ook?`          | `[`                   | Início de um laço                      |
| `Ook? Ook!`          | `]`                   | Fim de um laço                         |

## Instalação

### Pré-requisitos

- Python 3.8 ou superior
- [uv](https://github.com/astral-sh/uv) (opcional, para rodar com ambiente isolado)

### Instruções

Clone o repositório e navegue até a pasta:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

## Como usar

### Para rodar um programa Ook!:

```bash
python interpretador_ook.py exemplos/hello_world.ook
```

### Para contar os tokens de um arquivo:

```bash
python count_ook_tokens.py exemplos/fibonacci.ook
```

### Para rodar os testes:

```bash
pytest -q
```

## Exemplos

Todos os exemplos estão disponíveis na pasta `exemplos/`:

- `hello_world.ook`: imprime "Hello, World!"
- `fibonacci.ook`: gera a sequência de Fibonacci
- `contador_simples.ook`: conta de 0 a 9
- `apresentando_trabalho.ook`: imprime a mensagem de apresentação do trabalho

## Referências

- [**Ook! Specification – Esolang Wiki**](https://esolangs.org/wiki/Ook!) — utilizada para mapear corretamente os comandos e suas equivalências com o Brainfuck.
- **Intérpretes de Brainfuck em Python** — serviram de base conceitual para estruturar o interpretador e a lógica de execução.
- **Código original e implementação**: 100% desenvolvidos pelo grupo. Nenhum código foi copiado diretamente de fontes externas.

## Estrutura do Código

- `interpretador_ook.py`: módulo principal. Contém a lógica de leitura do arquivo `.ook`, tradução para Brainfuck e execução.
- `count_ook_tokens.py`: script auxiliar para contar e exibir a quantidade de tokens Ook! em um arquivo.
- `tests/`: pasta de testes automatizados para validar os exemplos.
- `exemplos/`: programas de exemplo escritos na linguagem Ook!

## Etapas da Compilação

- **Léxica**: separação dos tokens válidos do Ook!
- **Sintática**: verificação da ordem correta dos tokens em pares
- **Semântica**: tradução correta para instruções Brainfuck e execução do resultado

## Bugs, Limitações e Melhorias Futuras

- A linguagem não possui sistema de tipos nem estrutura de controle além de laços.
- Não há tratamento de erros para programas com tokens malformados ou desequilíbrio de colchetes.

**Futuras melhorias:**

- Adicionar suporte à depuração (modo passo a passo)
- Implementar mensagens de erro mais descritivas
- Suporte a leitura de entrada padrão diretamente
