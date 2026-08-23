from .module import root
from .folder_class import Class
# object is an hardcoded base in Abstract (method doesn't use super but directly use object)
Abstract = Class(object, root / "Abstract", body=dict(
    __slots__ = ('__weakref__', '__core__')))