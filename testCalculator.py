from calculator import * 
import unittest 

# class to test the calculator functionality
class TestCalculator(unittest.TestCase):

    # setup the test class 
    def setUp(self):
        self.calc = Calculator()
    
    # function to test the addition function 
    def testAdd(self):
        # test two positive numbers
        result = self.calc.add(1,1)
        self.assertEqual(2, result)
        # test positive number an zero
        result = self.calc.add(1, 0)
        self.assertEqual(1, result)
        # test positive and negative numbers 
        result = self.calc.add(-2, 1)
        self.assertEqual(-1, result)
        # test two negative numbers
        result = self.calc.add(-3, -4)
        self.assertEqual(-7, result)
        # test floating numbers
        result = self.calc.add(2.5, 1.2)
        self.assertEqual(3.7, result)
        # test long number 
        result = self.calc.add(1,1000000)
        self.assertEqual(1000001, result)
        # test string input
        result = self.calc.add('text1', 'text2')
        self.assertEqual(ValueError, result)
      
    # function to test the subtraction function 
    def testSubtract(self):
        # test two positive numbers
        result = self.calc.subtract(5,3)
        self.assertEqual(2, result)
        # test positive number and zero 
        result = self.calc.subtract(3,0)
        self.assertEqual(3, result)
        # test that returns a negative number 
        result = self.calc.subtract(2,3)
        self.assertEqual(-1, result)
        # test two negative numbers 
        result = self.calc.subtract(-5,-3)
        self.assertEqual(-2, result)       
        # test floating numbers
        result = self.calc.subtract(5.2,3.1)
        self.assertEqual(2.1, result)
        # test long number 
        result = self.calc.subtract(1000000,1)
        self.assertEqual(999999, result)
        # test string input
        result = self.calc.subtract('text', 'text2')
        self.assertEqual(ValueError, result)
		
	
    # function to test the multiplication function 
    def testMultiply(self):
        # test two positive numbers 
        result = self.calc.multiply(2,1)
        self.assertEqual(2, result)
        # test positive number and zero 
        result = self.calc.multiply(0,1)
        self.assertEqual(0, result)
        # test positive and negative number
        result = self.calc.multiply(-2,1)
        self.assertEqual(-2, result)
        # test two negative numbers 
        result = self.calc.multiply(-2,-1)
        self.assertEqual(2, result)
        # test floating numbers 
        result = self.calc.multiply(5.2, 4.0)
        self.assertEqual(20.8, result)
        # test long number 
        result = self.calc.multiply(2,1000000)
        self.assertEqual(2000000, result)
        # test string input
        result = self.calc.multiply('text', 'text2')
        self.assertEqual(ValueError, result)
     
    # function to test the division function 
    def testDivide(self):
        # test two positive numbers 
        result = self.calc.divide(5,2)
        self.assertEqual(2.5, result)
        result = self.calc.divide(4,2)
        self.assertEqual(2, result)
        # test positive number and zero 
        result = self.calc.divide(5,0)
        self.assertEqual('Cannot divide by zero', result)
        # test positive and negative numbers 
        result = self.calc.divide(5,-2)
        self.assertEqual(-2.5, result)
        # test two negative numbers 
        result = self.calc.divide(-5,-2)
        self.assertEqual(2.5, result)
        # test floating numbers 
        result = self.calc.divide(6.4,2.0)
        self.assertEqual(3.2, result)
        # test long number 
        result = self.calc.divide(2000000,2)
        self.assertEqual(1000000, result)
        # test string input
        result = self.calc.divide('text','text')
        self.assertEqual(ValueError, result)
        
    # function to test the add function # function to test the exponent function     
    def testExponent(self):
        # test exponent of 0
        result = self.calc.exponent(2,0)
        self.assertEqual(1, result)
        # test exponent of 1 
        result = self.calc.exponent(2,1)
        self.assertEqual(2, result)
        # test exponent squared
        result = self.calc.exponent(2,2)
        self.assertEqual(4, result) 
        # test exponent cubed
        result = self.calc.exponent(2,3)
        self.assertEqual(8, result)
        # test negative number squared 
        result = self.calc.exponent(-2,2)
        self.assertEqual(4, result)
        # test negative number squared 
        result = self.calc.exponent(-2,3)
        self.assertEqual(-8, result)
        # test negative exponent
        result = self.calc.exponent(2,-3)
        self.assertEqual(0.125, result)
        # test floating number 
        result = self.calc.exponent(2.0,2)
        self.assertEqual(4, result)
        # test floating exponent
        result = self.calc.exponent(2,2.0)
        self.assertEqual(4, result)
        # test zero 
        result = self.calc.exponent(0,2)
        self.assertEqual(0, result)
        # test string input 
        result = self.calc.exponent('text','text')
        self.assertEqual(ValueError, result)
     
    # function to test the factorial function 
    def testFactorial(self):
        # test 2!
        result = self.calc.factorial(2)
        self.assertEqual(2, result)
        # test 5!
        result = self.calc.factorial(5)
        self.assertEqual(120, result)
        # test 10!
        result = self.calc.factorial(10)
        self.assertEqual(3628800, result)
        # test 0!
        result = self.calc.factorial(0)
        self.assertEqual(1, result)
        # test factorial of negative number 
        result = self.calc.factorial(-2)
        self.assertEqual(None, result)
        # test factorial of floating number 
        result = self.calc.factorial(2.0)
        self.assertEqual(2, result)
        # test string input 
        result = self.calc.factorial('text')
        self.assertEqual(ValueError, result)
      
    # function to test the average function 
    def testAverage(self):
        # test two positive numbers
        result = self.calc.average(4,2)
        self.assertEqual(3, result)
        result = self.calc.average(1,2)
        self.assertEqual(1.5, result)
        # test positive number and zero 
        result = self.calc.average(4,0)
        self.assertEqual(2, result)
        # test positive and negative numbers 
        result = self.calc.average(4,-2)
        self.assertEqual(1, result)
        # test two negative numbers 
        result = self.calc.average(-3,-2)
        self.assertEqual(-2.5, result)
        # test floating numbers 
        result = self.calc.average(4.5,2.2)
        self.assertEqual(3.35, result)
        # test long number 
        result = self.calc.average(10,1000000)
        self.assertEqual(500005, result)
        # test string input
        result = self.calc.average('text','text')
        self.assertEqual(ValueError, result)
        
    # function to test the squareRoot function     
    def testSquareRoot(self):
        # test positive numbers 
        result = self.calc.squareRoot(9)
        self.assertEqual(3, result)
        result = self.calc.squareRoot(25)
        self.assertEqual(5, result)
        # test floating number
        result = self.calc.squareRoot(25.0)
        self.assertEqual(5, result)
        # test negative number 
        result = self.calc.squareRoot(-25)
        self.assertEqual(None, result)
        # test zero 
        result = self.calc.squareRoot(0)
        self.assertEqual(None, result)
        # test long number 
        result = self.calc.squareRoot(1000000)
        self.assertEqual(1000, result)
        # test string input
        result = self.calc.squareRoot('text')
        self.assertEqual(ValueError, result)
     
    # function to test the sine function  
    def testCalcSin(self):
        # test positive number
        result = self.calc.calcSin(45)
        self.assertEqual(0.70711, result)
        result = self.calc.calcSin(50)
        self.assertEqual(0.76604, result)
        result = self.calc.calcSin(60)
        self.assertEqual(0.86603, result)
        result = self.calc.calcSin(90)
        self.assertEqual(1, result)
        # test floating number 
        result = self.calc.calcSin(60.0)
        self.assertEqual(0.86603, result)
        # test zero 
        result = self.calc.calcSin(0)
        self.assertEqual(0, result)
        # test negative number
        result = self.calc.calcSin(-10)
        self.assertEqual(None, result)
        # test string input 
        result = self.calc.calcSin('text')
        self.assertEqual(ValueError, result)
    
    # function to test the cosine function     
    def testCalcCos(self):
        # test positive number 
        result = self.calc.calcCos(45)
        self.assertEqual(0.70711, result)
        result = self.calc.calcCos(50)
        self.assertEqual(0.64279, result)
        result = self.calc.calcCos(60)
        self.assertEqual(0.5, result)
        result = self.calc.calcCos(90)
        self.assertEqual(0, result)
        # test floating number
        result = self.calc.calcCos(60.0)
        self.assertEqual(0.5, result)
        # test zero 
        result = self.calc.calcCos(0)
        self.assertEqual(1, result)
        # test negative number
        result = self.calc.calcCos(-10)
        self.assertEqual(None, result)
        # test string input 
        result = self.calc.calcCos('text')
        self.assertEqual(ValueError, result)
        
    # function to test the tangent function    
    def testCalcTan(self):   
        # test positive number 
        result = self.calc.calcTan(45)
        self.assertEqual(1, result)
        result = self.calc.calcTan(50)
        self.assertEqual(1.19175, result)
        result = self.calc.calcTan(60)
        self.assertEqual(1.73205, result)
        result = self.calc.calcTan(90)
        self.assertEqual(None, result)
        # test floating number 
        result = self.calc.calcTan(60.0)
        self.assertEqual(1.73205, result)
        # test zero 
        result = self.calc.calcTan(0)
        self.assertEqual(0, result)
        # test negative number 
        result = self.calc.calcTan(-10)
        self.assertEqual(None, result)
        # test string input 
        result = self.calc.calcTan('text')
        self.assertEqual(ValueError, result)
        
# this is only run from the command line 
if __name__ == '__main__':
    # runs any subclasses that use unit tests
    unittest.main()
