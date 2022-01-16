
class fraction:
    
    def __init__(self , s=0 , m=1):
        self.numerator = s
        if self.denominator == 0:
            m=1
        self.denominator = m

    def sum(self,secondfra):
        result = fraction()
        result.numerator = self.numerator * secondfra.denominator + secondfra.numerator * self.denominator
        result.denominator = self.denominator * secondfra.denominator
        return result

    def sub(self,secondfra):
        result = fraction()
        result.numerator = self.numerator * secondfra.denominator - secondfra.numerator * self.denominator
        result.denominator = self.denominator * secondfra.denominator
        return result
        
    def mul(self, secondfra):
        result = fraction()
        result.numerator = self.numerator * secondfra.numerator
        result.denominator = self.denominator * secondfra.denominator 
        return result

    def div(self,secondfra):
        result = fraction()
        result.numerator = self.numerator * secondfra.denominator
        result.denominator = self.denominator * secondfra.numerator
        return result

    def show(self):
        print(self.numerator , '/' , self.denominator)


def input_fraction():
    numerator = int(input('enter numerator:'))
    denominator = int(input('enter denominator:'))
    return fraction(numerator,denominator)

a = input_fraction()
a.show()

b = input_fraction()
b.show()

c = a.mul(b)
c.show()

d = a.sum(b)
d.show()

e = a.sub(b)
e.show()

f = a.div(b)
f.show()