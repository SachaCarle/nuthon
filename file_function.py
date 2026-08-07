from pathlib import Path

def function(path, name=..., globals=..., locals=..., **kw):
    if not isinstance(path, Path): path = Path(path)
    if name is ...: name = path.stem
    script = path.read_text()
    lines = script.split("\n")
    script = f"""{'\n'.join(('' for _ in range(0, 99)))}
def {name}(*args, **kwargs):
    {'\n    '.join(lines)}"""
    code = compile(script, f"<{path}>", 'exec', **kw)
    if globals is ...: globals = dict()
    if locals is ...: locals = dict()
    exec(code, globals=dict(), locals=locals)
    print ("file_function.py", locals[name])
    return locals[name]