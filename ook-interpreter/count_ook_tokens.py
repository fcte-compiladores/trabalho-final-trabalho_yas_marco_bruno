import re

with open("/home/ubuntu/ook-interpreter/exemplos/contador.ook", "r", encoding="utf-8-sig") as file:
    code = file.read()

tokens = re.findall(r"Ook[.?!]", code)
print(f"Número de tokens Ook! encontrados: {len(tokens)}")


