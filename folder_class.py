from functools import partial
from types import new_class
from typing import Any
from .file_function import Path, function

if False: # This is the code to prevent abstract class to be instancied... I need to find where to put it...
            name = self.__class__.__name__
            body = self.__dict__
            for key, value in body.items():
                print ("<zfdjn>\t", key, value)
                if hasattr(value, '__isabstractmethod__'):
                    input(f"HELLO {body}")
                    if value.__isabstractmethod__:
                        raise NotImplementedError(f"Folder-Class {name} has not implemented abstract method {key}.")

class folder_meta(type):
    def __init__(self, *args):
        super().__init__(*args)

    def __call__(self, *args, **kwargs):
        print ("Here's the __init__ right ??", args, kwargs)
        return super().__call__(*args, **kwargs)

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
    if "__bases__" in body.keys(): raise Exception("Unexpected __bases__")
    else: body['__bases__'] = bases
    for fp in path.glob('*.py'):
        key = fp.stem
        body[key] = function(fp, key, globals=body, **kw)
    klass = new_class(name, bases=bases, kwds=dict(metaclass=folder_meta) if meta_args is None else meta_args,
        exec_body=lambda kb: kb.update(body))
    return klass
