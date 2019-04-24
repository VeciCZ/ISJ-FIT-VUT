#!/usr/bin/env python3

def factorial(num):
    '''
    Return factorial of a number using recursion.
    '''
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

class Polynomial():
    '''
    Definition of a class to represent a polynomial and operations with it.
    '''
    
    def __init__(self, *argv, **kwarg):
        '''
        Initialize a list with the polynomial values, which may be given in various ways. 
        '''

        self.values = []
        self.emptypol = False

        # determine type of polynomial and store it in a list, if it already isn't one
        if len(argv) > 0:
            if type (argv[0]) == list:
                self.values.extend(argv[0])
            else:
                for i in range(len(argv)):
                    self.values.append(argv[i])
        else:
            if kwarg is not None:
                    kwarg = sorted(kwarg.items(), reverse=True)
                    for key, value in kwarg:
                        maxnum = int(key[1:]) + 1
                        break
                    
                    self.values = [0] * maxnum
                    
                    for key, value in kwarg:
                        self.values[int(key[1:])] = value
                    if sum(self.values) == 0:
                        self.emptypol = True

    def __repr__(self):
        '''
        Return polynomial as a string in human readable form.
        '''
        
        polyprint = ""
        if self.emptypol == True:
            return "0"

        i = len(self.values)-1
        valuelst = self.values[::-1]

        # gradually concatenate string with polynomial 
        for item in range(len(valuelst)):
            num = valuelst[item]
            if num == 0:
                i = i - 1
                continue
            else:
                if num < -1:
                    polyprint += " - " + str(abs(num))
                elif num == -1:
                    polyprint += " - "
                elif num == 1:
                    polyprint += " + "
                else:
                    polyprint += " + " + str(num)

                if i > 1:
                    polyprint += "x^" + str(i)
                elif i == 1:
                    polyprint += "x"
                elif i == 0 and str(num) != polyprint[-1] and num > -2:
                    polyprint += str(abs(num))

                i = i - 1

        if polyprint[1] == '-':
            polyprint = polyprint[1:]
        elif polyprint[1] == '+':
            polyprint = polyprint[3:]
            
        return polyprint

    def __eq__(self, other):
        '''
        Equality of polynomials.
        '''
        return sum(self.values) == sum(other.values)

    def __ne__(self, other):
        '''
        Inequality of polynomials.
        '''
        return self.values != other.values

    def __add__(self, other):
        '''
        Add one polynomial to another.
        '''
        x = self.values
        y = other.values

        # make polynomial list x always longer than y
        if len(x) < len(y):
            temp = x
            x = y
            y = temp
            
        result = []
        i = 0

        # make both polynomials the same length and add them
        for i in range(len(x) - len(y)):
            y.append(0)
        for num in x:
            result.append (num + y[i])
            i += 1
            
        return Polynomial(result)

    def __pow__(self, num):
        '''
        Exponentiate given polynomial using the binomial theorem.
        '''
        polypow = [0] * (num+1)
        i = len(polypow)-1
        for item in polypow:
            polypow[i] = int((factorial(num)/(factorial(i)*factorial(num-i))) * \
                         (self.values[-2]**i) * (self.values[-1]**i))
            i -= 1
            
        return Polynomial(polypow[::-1])        
        
    def derivative(self):
        '''
        Derive polynomial.
        '''
        if len(self.values) == 1:
            return "0"
        i = len(self.values)-1
        der = [0] * (i+1)

        for item in self.values[::-1]:
            if i == 0:
                break
            der[i-1] = item * i
            i -= 1
        
        return Polynomial(der)

    def at_value(self, *argv):
        '''
        Count the value of a polynomial for a certain number as x. If two numbers are set,
        calculate the value for each of them and substract the first from the second.
        '''
        def val(values, num):
            '''
            Main function code in nested function to avoid repetitive code in main function.
            '''
            valuelst = values[::-1]
            i = len(valuelst)-1
            sum = 0
            for item in valuelst:
                sum += (item * num**i)
                i -= 1
            return sum

        if len(argv) == 1:
            return val(self.values, argv[0])
        else:
            return ( val(self.values, argv[1]) - val(self.values, argv[0]) )


def test():
    '''
    Assert statements to test functionality of Polynomial class.
    '''
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
