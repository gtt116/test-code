import traceback

try:
    print 'a'
    raise Exception()
except Exception:
    print traceback.print_exc()
    print '-----------'
    print traceback.print_stack()
    print '-----------'
