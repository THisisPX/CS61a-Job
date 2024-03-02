from math import pi , sqrt

def sum_naturals(n):
        """Return the sum of the first n natural numbers.

        >>> sum_naturals(10)
        55
        >>> sum_naturals(100)
        5050
        """
        return summation(n,identity)

def identity(n):
      return n

def cube(n):
      return pow(n,3)



def summation(n,term):
        """Sum the4 first N terms

        >>> sum_naturals(5,cube)
        255
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + term(k), k + 1
        return total


print('lalla')

def make_adder(n) :
      """ return  a function that 

      >>> add_three = make_adder(3)
      >>> add_three(4)
      7
      """
      def adder(k) :
            return k+n
      return adder

def has_big_sqrt(x):
      return x >10 and sqrt(x) > 10
def reasonable(n):
      return 1/n != 0 or n == 0

def abs(x) :
      if x >= 0 :
            return x
      else :
            return -x

def how_big(x):
     if x > 10:
         print('huge')
     elif x > 5:
         return 'big'
     elif x > 0:
         print('small')
     else:
         print("nothin'")
       
positive = 28
while positive: # If this loops forever, just type Infinite Loop
    print("positive?")
    positive -= 3
