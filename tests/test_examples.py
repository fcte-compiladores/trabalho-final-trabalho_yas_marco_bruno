import pathlib
import sys
import re
import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))


from interpretador_ook import tokenize_ook, read_ook_code  # noqa: E402

EXAMPLES_DIR = pathlib.Path(__file__).resolve().parent.parent / "exemplos"


@pytest.mark.parametrize(
    "filename",
    ["contador.ook", "contador_simples.ook", "hello.ook", "test_simple.ook"],
)
def test_tokenize_example_files(filename):
    path = EXAMPLES_DIR / filename
    code = read_ook_code(path)

    raw_tokens = re.findall(r"Ook[.?!]", code)
    assert len(raw_tokens) % 2 == 0 and len(raw_tokens) > 0

    bf_tokens = tokenize_ook(code)

    assert len(bf_tokens) == len(raw_tokens) // 2

    for cmd in bf_tokens:
        assert cmd in "><+-.,[]"

