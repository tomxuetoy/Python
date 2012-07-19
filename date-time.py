from datetime import datetime

def foo():
    d = datetime.now()
    print d
    print d.ctime()

foo()
