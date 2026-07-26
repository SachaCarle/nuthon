from pathlib import Path

def function(path, name=..., globals=..., locals=..., **kw):
    if not isinstance(path, Path): path = Path(path)
    if name is ...: name = path.stem
    script = path.read_text()
    lines = script.split("\n")
    script = f"""def {name}(*args, **kwargs):
    {'\n    '.join(lines)}"""
    code = compile(script, f"<{path}>", 'exec', **kw)
    if globals is ...: globals = dict()
    if locals is ...: locals = dict()
    exec(code, globals=dict(), locals=locals)
    return locals[name]