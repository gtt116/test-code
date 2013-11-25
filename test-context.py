class ContextTest(object):
    def __init__(self):
        print 'init'

    def __enter__(self):
        print 'enter'

    def __exit__(self, *args, **kwargs):
        print 'exit. with args: %s, kwargs: %s' % (args, kwargs)


print '----------'
with ContextTest() as context:
    print 'I am inner'

print '----------'
with ContextTest() as context:
    print 'I am another inner, but raise exception'
    try:
        raise Exception("Rock the world")
    except Exception:
        print "I eaten the exception, so context does't see it"

print '----------'
with ContextTest() as context:
    print 'I am another inner, but raise exception'
    raise Exception("Rock the world")
