self, other = args
if isinstance(other, str):
    try: return getattr(self, other)
    except: return None
else: raise NotImplementedError(self, '-', type(other))