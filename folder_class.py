from .file_function import Path, function

def Class(path, name=..., bases=(), globals=..., **kw):
    print ("nuthon/folder_class.py(Class)", path)
    if not isinstance(path, Path): path = Path(path)
    if name is ...: name = str(path).replace('/', '_').replace('\\', '_')
    body = {}
    for fp in path.glob('*.py'):
        key = str(fp).replace('.py', '').replace('/', '_').replace(f'{name}\\', '')
        print ("#653\t", fp, '->', key)
        input()
        body[key] = function(fp, name, globals=globals, **kw)
    klass = type(name, bases, body, **kw)
    return klass
    
    
    
    
    
    
    
    
    