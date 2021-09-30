import lab1 as c

class FooCalculator:

    def __init__(self):
        pass

    def sum(self,m,n):
        return c.sum(m,n)

    def divide(self,m,n):
        return c.divide(m,n)

FC = FooCalculator()

m = int(input("Insert m: "))
n = int(input("Insert n: "))

print("The sum provides:", FC.sum(m,n))
print("The division provides:",FC.divide(m,n))