class MyException(Exception):pass # pass: define a empty class
try:
    print "normal code here"
except MyException:
    print "MyException encoutered"
else:
    print "No exception"
finally:
    print "Arrive finally"
