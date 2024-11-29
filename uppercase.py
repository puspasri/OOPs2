class IOstring:

    def __init__(self):
        self.str1=" "

    def getstring(self):
        self.str1=input("enter the name ")


    def printstring(self):
        print(" result is ", self.str1.upper())
        #()-IOstring
name = IOstring()
name.getstring()
name.printstring()



