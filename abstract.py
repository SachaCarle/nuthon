from .module import root
from .folder_class import Class
Abstract = Class(object, root / "Abstract", body=dict(
            __slots__ = ('__weakref__', '__core__')))