if False: # can use the 'file' named argument to use print to
    print('Second line.', file=output) # write into file easy
    # Wille be VERY usefull when expanding logging capacities

class printer:
    def __init__(self, flag, *args, activate=True, **kwargs):
        if flag is ...:
            self.parts = Ellipsis
        elif '/' in flag:
            self.parts = flag.split('/')
            self.args = args
        else:
            self.args = (flag, *args)
            self.parts = ()
        self.kwargs = kwargs
        self.activate = activate

    def rl(self):
        if not self.activate: return
        print ()

    def __call__(self, flag, *args, **kwargs):
        if not self.activate: return
        if not isinstance(flag, str): flag = str(flag)
        if self.parts is Ellipsis:
            return print (flag, *args, **kwargs)
        parts = (*self.parts, *flag.split('/'))
        args = (*self.args, *args)
        kwargs = {**self.kwargs, **kwargs}
        # TODO: parts-sensible filtering of logs
        if len(args) <= 1: print ('\n', '/'.join(parts), *args, **kwargs)
        else: print ('\n', '/'.join(parts), "\n\t", *args, **kwargs)
