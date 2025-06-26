result =0
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b

x = Calculator(1,2)
print("-----------------")
print(x.add())
y = Calculator(1,3)
print("-----------------")
print(y.add())
z = Calculator(4,2)
print("-----------------")
print(z.add())


print(type(x))

def add(a,b):
    result = a+b
    return result

x = add(4,3)
print(x)

