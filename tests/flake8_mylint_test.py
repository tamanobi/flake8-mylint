import ast
from typing import Set
from flake8_mylint import Plugin

def _result(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f"{line}:{col} {msg}" for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _result("") == set()
