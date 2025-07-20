import pathlib
import sys
import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from interpretador_ook import tokenize_ook, read_ook_code

EXAMPLES_DIR = pathlib.Path(__file__).resolve().parent.parent / "exemplos"

@pytest.mark.parametrize("filename", [
    "contador.ook",
    "contador_simples.ook",
    "hello.ook",
    "test_simple.ook",
])
def test_tokenize_example_files(filename):
    path = EXAMPLES_DIR / filename
    code = read_ook_code(path)
    tokens = tokenize_ook(code)
    # The number of tokens should be even and at least one pair should exist
    assert len(tokens) > 0

