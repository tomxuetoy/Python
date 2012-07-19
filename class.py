class Person:
        def __init__(self,name):
                self.name=name
        def hiSay(self):
                print 'hello,',self.name
p=Person('Tom Xue')
p.hiSay()
