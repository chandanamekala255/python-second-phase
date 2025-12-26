class Alpha:
    def fun1(self):
        print(" i am an Alpha")

class Beta:
    def fun2(self):
        print(" iam beta")
class Gamma(Alpha,Beta):
     pass 
g.Gamma()
g.fun1()
g.fun2()
