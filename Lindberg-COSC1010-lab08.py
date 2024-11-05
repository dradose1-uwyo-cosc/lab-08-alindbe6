# Adam Lindberg
# UWYO COSC 1010
# 11/5/24
# Lab 10
# Lab Section: 10
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def check_string(num):
    """Checks string for int or float, converts."""
    isNeg = False
    if num[0] == "-":
        isNeg = True
        num = num.replace("-","")
    if "." in num:
        nums = num.split(".")
        if len(nums) == 2 and nums[0].isdigit() and nums[1].isdigit():
            if isNeg:
                return -1 * float(num)
            else:
                return float(num)
    elif num.isdigit():
        if isNeg:
            return -1 * int(num)
        else:
            return int(num)
    else:
        return False
    

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

def slope_intercept(m, b, lower_x, upper_x):
    """Calculates outupts in range of x."""

    if type(lower_x) != int or type(upper_x) != int:
        return False
    if lower_x < upper_x:
        output = []
        for x in range(lower_x,upper_x+1):
            y = (m * x) + b
            output.append(y)
    return output


# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
while True:
    variables = input("Type in values for m, b, lower x bound and an upper x bound here:\n")

    if variables.lower() == "exit":
        break
    variables = variables.replace(" ","")
    variables = variables.split(",")
    m = check_string(variables[0])
    b = check_string(variables[1])
    lower_x = check_string(variables[2])
    upper_x = check_string(variables[3])
    result = slope_intercept(m,b,lower_x,upper_x)
    print(result)
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
null = None
def square_root(num):
    """Finds square root of a number."""
    if num < 0:
        return null
    else:
        return num**0.5
def quad_roots(a, b, c):
    """Finds the real roots of a quadratic of the form ax^2+bx+c."""
    a = check_string(a)
    b = check_string(b)
    c = check_string(c)
    if square_root(b**2-(4*a*c)) != null:
        root1 = (-b + square_root(b**2-(4*a*c)))/(2 * a)
        root2 = (-b - square_root(b**2-(4*a*c)))/(2 * a)
        roots = [root1, root2]
        return roots
    else:
        return null


while True:
    prompt = input("Input values for a,b, and c here:\n")
    if prompt.lower() == "exit":
        break
    prompt = prompt.replace(" ","")
    prompt = prompt.split(",")
    a = prompt[0]
    b = prompt[1]
    c = prompt[2]
    print(quad_roots(a, b, c))