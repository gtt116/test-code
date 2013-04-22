import sys


def c():
    print 'c'

def b():
    print 'b'
    c()

def a():
    import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
    ff = sys._getframe()
    print 'a'
    b()


a()
