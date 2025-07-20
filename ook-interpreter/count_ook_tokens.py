import re
import sys
from pathlib import Path


def main(path: str) -> None:
    file_path = Path(path)
    with open(file_path, "r", encoding="utf-8-sig") as file:
        code = file.read()



    tokens = re.findall(r"Ook[.?!]", code)
    print(f"Número de tokens Ook! encontrados: {len(tokens)}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        # Use one of the sample programs as the default
        default = Path(__file__).parent / "exemplos" / "contador.ook"


    tokens = re.findall(r"Ook[.?!]", code)
    print(f"Número de tokens Ook! encontrados: {len(tokens)}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        # Use one of the sample programs as the default
        default = Path(__file__).parent / "exemplos" / "contador.ook"
        main(default)
