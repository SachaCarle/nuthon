from functools import partial
from types import new_class
from typing import Any
from .file_function import Path, function

class folder_meta(type):
    def __init__(self, *args):
        super().__init__(*args)

    def __call__(self, *args, **kwargs):
        name = self.__name__
        body = self.__dict__
        abstracts = []
        abstract_bases = []
        for key, value in body.items():
            if hasattr(value, '__isabstractmethod__'):
                if value.__isabstractmethod__:
                    raise NotImplementedError(f"Can't instantiate abstract class {self.__name__}")
        if hasattr(self, '__bases__'):
            for base in self.__bases__:
                for key, value in base.__dict__.items():
                    if hasattr(value, '__isabstractmethod__'):
                        if value.__isabstractmethod__:
                            if hasattr(body, key) and not getattr(body, key).__isabstractmethod__: continue
                            else:
                                abstracts.append(key)
                                if not (base.__name__ in abstract_bases):
                                    abstract_bases.append(base.__name__)
        if len(abstracts):
            raise NotImplementedError(f"{name} has not implemented abstract method {', '.join(abstracts)} defined in {', '.join(abstract_bases)}.")
        # ABSTRACT METHOD VERIFICATION
        instance = super().__call__(*args, **kwargs)
        return instance

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
