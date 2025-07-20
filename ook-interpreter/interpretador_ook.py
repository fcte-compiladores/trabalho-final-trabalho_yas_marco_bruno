import re
import sys

OOK_TO_BF = {
    ("Ook.", "Ook?"): ">",
    ("Ook?", "Ook."): "<",
    ("Ook.", "Ook."): "+",
    ("Ook!", "Ook!"): "-",
    ("Ook!", "Ook."): ".",
    ("Ook.", "Ook!"): ",",
    ("Ook!", "Ook?"): "[",
    ("Ook?", "Ook!"): "]",
}


def read_ook_code(path):
    with open(path, 'r', encoding='utf-8-sig') as file:
        text = file.read()
    return text


def tokenize_ook(code):
    # Remove comments (anything after #)
    code = re.sub(r"#.*$", "", code, flags=re.MULTILINE)

    # Normalize Unicode (NFKC is generally good for compatibility)
    import unicodedata
    code = unicodedata.normalize("NFKC", code)

    # Trim whitespace that might interfere with tokenization
    code = code.strip()

    # Find all Ook tokens, case-insensitive
    tokens = re.findall(r"Ook[.?!]", code)

    print(f"[DEBUG] Total de tokens encontrados: {len(tokens)}")
    print(f"[DEBUG] Primeiros 5 tokens: {tokens[:5]}")
    print(f"[DEBUG] Últimos 5 tokens: {tokens[-5:]}")

    if len(tokens) % 2 != 0:
        # Print all tokens to debug the odd count
        print(f"[DEBUG] Todos os tokens: {tokens}")
        raise SyntaxError(
            f"Número ímpar de tokens Ook!: {len(tokens)} encontrados"
        )

    bf_tokens = []
    for i in range(0, len(tokens), 2):
        pair = (tokens[i], tokens[i+1])
        if pair not in OOK_TO_BF:
            raise SyntaxError(
                f"Comando inválido: {pair[0]} {pair[1]} (par na posição {i})"
            )
        bf_tokens.append(OOK_TO_BF[pair])
    return bf_tokens


def run_brainfuck(code):
    tape = [0] * 30000
    ptr = 0
    pc = 0
    jump_map = {}

    # mapa de saltos (pré-processa colchetes)
    temp_stack = []
    for pos, cmd in enumerate(code):
        if cmd == '[':
            temp_stack.append(pos)
        elif cmd == ']':
            if not temp_stack:
                raise SyntaxError("']' sem '[' correspondente")
            start = temp_stack.pop()
            jump_map[start] = pos
            jump_map[pos] = start
    if temp_stack:
        raise SyntaxError("'[' sem ']' correspondente")

    while pc < len(code):
        cmd = code[pc]
        if cmd == '>':
            ptr += 1
            if ptr >= len(tape):
                ptr = 0  # Wrap around
        elif cmd == '<':
            ptr -= 1
            if ptr < 0:
                ptr = len(tape) - 1  # Wrap around
        elif cmd == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '.':
            print(chr(tape[ptr]), end='')
        elif cmd == ',':
            try:
                tape[ptr] = ord(input("Entrada: ")[0])
            except Exception:
                tape[ptr] = 0
        elif cmd == '[' and tape[ptr] == 0:
            pc = jump_map[pc]
        elif cmd == ']' and tape[ptr] != 0:
            pc = jump_map[pc]
        pc += 1


def main():
    if len(sys.argv) != 2:
        print("Uso: python interpretador_ook.py arquivo.ook")
        return

    path = sys.argv[1]
    try:
        code = read_ook_code(path)
        bf_code = tokenize_ook(code)
        run_brainfuck(bf_code)
    except Exception as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
