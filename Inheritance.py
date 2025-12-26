class Alpha:
    def fun1(self):
        print("i am an Alpha")

class Beta(Alpha):
    pass

b = Beta()
b.fun1()

#output: i am an Alpha
