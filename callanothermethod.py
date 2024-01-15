#1 Class defination is one time process
class MyClass():
    #1. Property/Variable
    name=''
    surname=""
    #2. Constructor/Esp.Function
    def __init__(self,n,s):
        print(1)
        self.name=n #Initailize
        self.surname=s #Initailize
        #print("Accessed with internal object i.e self",self.name,self.surname)#I have Initailize the value with the help of internal object
        #calling another method
        self.myMethod2()
        pass
    #3. Function/Method
    def myMethod1(self):#self=cio
        print(2)
        
        pass
    def myMethod2(self):#self=cio
        print(3)
        self.myMethod1()
        pass
    pass
#2 create class object is many time process
ceo1=MyClass("Vishal",'Mahawar')
#print('Accessed with external object ',ceo1.name,ceo1.surname)# access the property of with the help of external object