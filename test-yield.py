def iter():

    for i in xrange(0,100):
        print 'before'
        yield i
        print 'after'

g = iter()
g.next()
print '-'
g.next()
