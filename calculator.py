import unittest 
import math

# class with calculator functions
class Calculator(object):
 
    # function to add two numbers 
    def add(self, num1,num2):
        number_types = (int, long, float) 
        # check numbers are a required number type
        if isinstance(num1, number_types) and isinstance(num2, number_types):
            return num1 + num2
        else:
            return ValueError
    
    # function to subtract two numbers 
    def subtract(self, num1,num2):
        number_types = (int, long, float) 
        if isinstance(num1, number_types) and isinstance(num2, number_types):
            return num1 - num2
        else:
            return ValueError
    
    # function to multiply two numbers 
    def multiply(self, num1, num2):
        number_types = (int, long, float) 
        if isinstance(num1, number_types) and isinstance(num2, number_types):
            return num1 * num2
        else:
            return ValueError

    # function to divide two numbers
    def divide(self, num1, num2):
        number_types = (int, long, float) 
        if isinstance(num1, number_types) and isinstance(num2, number_types):
            # check that neither parameters are zero 
            if num1 == 0 or num2 == 0:
                return 'Cannot divide by zero'
            else:
                return float(num1)/float(num2)
        else:
            return ValueError
    
    # function to calculate an exponent
    def exponent(self, num, power):
        number_types = (int, float)
        if isinstance(num, number_types) and isinstance(power, number_types):
            return num ** power
        else:
            return ValueError 
            
    # function to calculate the factorial of a number 
    def factorial(self, num):
        number_types = (int, float)
        if isinstance(num, number_types):
            # if number is a float then it must be truncated to make it a whole number 
            if isinstance(num, float):
                num = math.trunc(num)
            # we perform checks in case it is zero or a negative number 
            if num == 0:
                return 1
            elif num < 0:
                return None
            # perform a recursive function to calculate the factorial  
            else:
                return num * Calculator.factorial(self,num-1)
        else:
            return ValueError 
        
    # function to calculate the average of two numbers 
    def average(self, num1, num2):
        number_types = (int, long, float) 
        if isinstance(num1, number_types) and isinstance(num2, number_types):
            # we use the add function to get the sum of the two numbers and then divide by two 
            return Calculator.add(self,num1,num2)/2.0
        else:
            return ValueError
    
    # function to calculate the square root of a number
    def squareRoot(self, num):
        number_types = (int, float)         
        if isinstance(num, number_types):
            # check number is greater than zero. If so call the maths function for the square root 
            if num > 0:
                return math.sqrt(num)
            else:
                return None
        else:
            return ValueError 
    
    # function to calculate the sine of an angle 
    def calcSin(self, x):
        number_types = (int, float) 
        if isinstance(x, number_types):
            # angle cannot be less than 0
            if x < 0:
                return None          
            else:
                 # convert from degrees to radians 
                rad = math.radians(x)
                # use the Maths function to calculate the sine, then round to 5 decimal places
                sin = round(math.sin(rad),5)
                return sin
        else:
            return ValueError
    
    # function to calculate the cosine of an angle 
    def calcCos(self, x):
        number_types = (int, float) 
        if isinstance(x, number_types):
            if x < 0:
                return None
            else:
                rad = math.radians(x)
                cos = round(math.cos(rad),5)
                return cos
        else:
            return ValueError

    # function to calculate the tangent of an angle 
    def calcTan(self, x):
        number_types = (int, float) 
        if isinstance(x, number_types):
            # as the tan of 90 has no value, we must also check for this 
            if x == 90 or x < 0:
                return None
            else:   
                rad = math.radians(x)
                tan = round(math.tan(rad),5)
                return tan 
        else:
            return ValueError
    
# this function does not belong to the calculator class as it is not used to make a calculation. It checks that the input is valid integer     
def validateInput(valueName):
    # this loop continues until a valid integer is entered
    while True:
        # tries to convert the input to a float. It returns the number if successful or gives an error if not 
        try:
            num = float(raw_input('Enter %s: ' % valueName))
        except:
            print 'Invalid input'
        else:
            return num 
            
                  
# this is only run from the command line 
if __name__ == '__main__':

    # instance of Calculator class 
    calc =  Calculator()
    # Menu shown to user 
    print '''Menu 
       Type 1 for addition function
       Type 2 for subtraction function 
       Type 3 for multiplication function
       Type 4 for division function 
       Type 5 for exponent function
       Type 6 for factorial function
       Type 7 for average function 
       Type 8 for square root 
       Type 9 for sin
       Type 10 for cos 
       Type 11 for tan
       Type 'q' to exit the program '''
    # continue looping until user decides to exit 
    while True: 
        # allow the user to input an option 
        input = raw_input('Option: ')
        # allow user to exit program by typing 'q'
        if input == 'q':
            break 
        # try to cast option input to integer 
        try:
            option = int(input)
        except:
            print 'Invalid input'
        else:
            # if number is less than 1 or greater than 11 then give an error   
            if option < 1 or option > 11:
                print 'Please enter a number between 1 and 11' 
            # for each of the following, check the option input, validate the number input and perform the option's function 
            elif option == 1:
                print 'Enter two numbers to add them'
                num1 = validateInput('number 1')
                num2 = validateInput('number 2')                             
                print calc.add(num1,num2)
            elif option == 2:  
                print 'Enter two numbers to subtract them'
                num1 = validateInput('number 1')
                num2 = validateInput('number 2')                    
                print calc.subtract(num1,num2)
            elif option == 3:
                print 'Enter two numbers to multiply them'
                num1 = validateInput('number 1')
                num2 = validateInput('number 2')
                print calc.multiply(num1,num2)
            elif option == 4:
                print 'Enter two numbers to divide them'
                num1 = validateInput('number 1')
                num2 = validateInput('number 2')
                print calc.divide(num1,num2)
            elif option == 5:
                print 'Enter a number and an exponent'
                num1 = validateInput('number')
                num2 = validateInput('exponent')
                print calc.exponent(num1,num2)
            elif option == 6:
                print 'Enter a number to calculate factorial'
                num = validateInput('number')
                print calc.factorial(num)
            elif option == 7:
                print 'Enter two numbers to calculate the average'
                num1 = validateInput('number 1')
                num2 = validateInput('number 2')
                print calc.average(num1,num2)
            elif option == 8:
                print 'Enter a number to get the square root'
                num = validateInput('number')
                print calc.squareRoot(num)
            elif option == 9:
                print 'Calculate the sine of an angle. Input degrees'
                angle = validateInput('angle degrees')
                print calc.calcSin(angle)
            elif option == 10:
                print 'Calculate the cosine of an angle. Input degrees'
                angle = validateInput('angle degrees')
                print calc.calcCos(angle)
            elif option == 11:
                print 'Calculate the tangent of an angle. Input degrees'
                angle = validateInput('angle degrees')
                print calc.calcTan(angle)
    