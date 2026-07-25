from pathlib import Path

def function(path, name=..., globals=..., locals=..., **kw):
    if not isinstance(path, Path): path = Path(path)
    if name is ...: name = str(path).replace('.py', '').replace('/', '_')
    script = path.read_text()
    lines = script.split("\n")
    script = f"""def {name}(*args, **kwargs):
    {'\n    '.join(lines)}"""
    #print (f"'{script}'")
    code = compile(script, f"<{path}>", 'exec', **kw)
    if globals is ...: globals = dict()
    if locals is ...: locals = dict()
    exec(code, globals=dict(), locals=locals)
    return locals[name]