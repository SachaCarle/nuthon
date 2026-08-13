from pathlib import Path

def function(path, name=..., globals=..., locals=..., **kw):
    if not isinstance(path, Path): path = Path(path)
    if name is ...: name = path.stem
    script = path.read_text()
    lines = script.split("\n")
    decorators = []
    while lines[0].startswith("#"):
        l = lines[0]
        if l.startswith("#@"):
            is_from = l.split(" from ")
            if len(is_from) == 2:
                name, module_path = is_from[0][2:], is_from[1]
                decorator_import = f"from {module_path} import {name}"
                container = dict()
                exec(decorator_import, globals=dict(), locals=container)
                decorators.append(container[name])
                lines = lines[1:]
            else: raise Exception(f"Unknow comment {l}")
        elif l.startswith("# "):
            lines = lines[1:]
        else: raise Exception(f"Unknow comment {l}")
    script = f"""{'\n'.join(('' for _ in range(0, 99)))}
def {name}(*args, **kwargs):
    {'\n    '.join(lines)}"""
    code = compile(script, f"<{path}>", 'exec', **kw)
    if globals is ...: globals = dict()
    if locals is ...: locals = dict()
    exec(code, globals=dict(), locals=locals)
    fun = locals[name]
    while len(decorators) > 0:
        fun = decorators.pop(0)(fun)
    return fun