class MyException(Exception):pass
try:
    raise MyException,", and some additional data"
except MyException,data2:   # here 'data2' is the placeholder for above sentence
    print "MyException encoutered"
    print data2
