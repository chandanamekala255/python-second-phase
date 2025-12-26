class Alpha:
    def fun1(self):
        print(" i am an Alpha")

class Beta(Alpha):
    def fun2(self):
        print(" iam beta")
class Gamma(Beta):
     pass 
g.Gamma()
g.fun1()
g.fun2()
#output: iam an Alpha 
#iam Beta

