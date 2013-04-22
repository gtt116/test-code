import sys

import os

def hello():
    sys.exit(1)

def hello_quici():
    os._exit(1)


try:
    hello()
except SystemExit:
    print 'hello die.'

try:
    hello_quici()
except Exception:
    print 'quici die.'
