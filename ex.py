class MyException(Exception):pass # pass: define a empty class
try:
    #some code here
    raise MyException             # it is empty, so it won't be raised in fact
except MyException:
    print "MyException encoutered"
finally:
    print "Arrive finally"
