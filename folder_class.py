from .file_function import Path, function

def Class(path, name=..., bases=(), globals=..., **kw):
    print ("nuthon/folder_class.py(Class)", path)
    if not isinstance(path, Path): path = Path(path)
    if name is ...: name = path.stem
    body = {}
    for fp in path.glob('*.py'):
        key = fp.stem
        body[key] = function(fp, name, globals=globals, **kw)
    klass = type(name, bases, body, **kw)
    return klass
    
    
    
    
    
    
    
    
    