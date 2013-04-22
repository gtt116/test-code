import inspect


def hello():
    print 'hello'
    frame_me = inspect.currentframe()
    print inspect.currentframe()
    print inspect.getframeinfo(frame_me)
    print inspect.stack()[0]
    print globals()['hello']


hello()
