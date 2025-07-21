# Ook Interpreter

This repository contains a minimal interpreter for the esoteric
programming language **Ook!**, implemented in Python. The interpreter
translates Ook! commands into Brainfuck instructions and then executes
them.

## Running an Ook program

Use the `interpretador_ook.py` script and provide the path to an `.ook`
file:

```bash
python interpretador_ook.py exemplos/hello.ook
```

Sample Ook programs are available in the `exemplos/` directory.

## Counting tokens

The `count_ook_tokens.py` script reads a program and prints the number
of Ook tokens it contains. You can pass a file path or let it use the
`contador.ook` example by default:

```bash
python count_ook_tokens.py
python count_ook_tokens.py exemplos/test_simple.ook
```

## Running the tests

A small test suite ensures that all example programs can be tokenized
and translated correctly. Run it with:

```bash
pytest -q
```

