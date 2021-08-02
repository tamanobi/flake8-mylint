import ast
import sys
from typing import Generator, Tuple, Type, Any, Union

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata

MSG = "FML100 use tuple instead of global list"

class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        program = []
        for child in ast.iter_child_nodes(self._tree):
            if (isinstance(child, ast.Assign) or isinstance(child, ast.AnnAssign)) and isinstance(child.value, ast.List):
                program.append((child.lineno, child.col_offset))

        for lineno, col in program:
            yield lineno, col, MSG, type(self)
