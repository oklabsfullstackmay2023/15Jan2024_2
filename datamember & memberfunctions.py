#1 class defination is one time process
class MyClass():
    #1. Property/Variable/Data member
    wheels=''
    bumpers=""
    exhaust=''''''
    #2.Constructor/Esp.Function
    def __init__(self):
        pass
    #3. Method/Function/member functions
    def speed(self):
        print("hello from speed method")
        pass
    def engine(self):
        print("Hello from engine method")
        pass
    def mileage(self):
        print("hello from mileage method")
        pass
    pass
#2 create class external object is many time process
ceo1=MyClass()
ceo1.speed()
ceo1.engine()
ceo1.mileage()