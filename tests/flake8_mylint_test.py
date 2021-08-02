import ast
from typing import Set
from flake8_mylint import Plugin

def _result(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f"{line}:{col + 1} {msg}" for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _result("") == set()

def test_incorrect_assign_list():
    assert _result("""t = ["hello", "world"]""") == {"1:1 FML100 use tuple instead of global list",}

def test_allow_assign_tuple():
    assert _result("""t = ("hello", "world")""") == set()

def test_allow_assign_in_function_and_class():
    """関数の中やクラスの中は無視する"""
    assert _result("""\
def sample():
    tmp = [1, 2]
    return tmp
class A():
    tmp = [1, 2]
""") == set()

def test_incorrect_annassign():
    assert _result("""\

t: List = [1,]
""") == {"2:1 FML100 use tuple instead of global list",}