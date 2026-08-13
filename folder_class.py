from functools import partial
from types import new_class
from typing import Any
from .file_function import Path, function

class folder_meta(type):
    def __getattribute__(self, key) -> Any:
        r = super().__getattribute__(key)
        if isinstance(self, type) and type(r).__name__ == "function":
            return partial(r, self)
        return r

def Class(bases, path, name=..., body=..., meta_args=None, **kw):
    if not isinstance(bases, (tuple, list)): bases = (bases, )
    if not isinstance(path, Path): path = Path(path)
    assert path.exists(), path
    if name is ...: name = path.stem
    if body is ...: body = {}
    for fp in path.glob('*.py'):
        key = fp.stem
        body[key] = function(fp, key, globals=body, **kw)
    klass = new_class(name, bases=bases, kwds=dict(metaclass=folder_meta) if meta_args is None else meta_args,
        exec_body=lambda kb: kb.update(body))
    return klass
