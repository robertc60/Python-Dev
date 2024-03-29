#
# Example file for working with functions
#

# Define a basic function
def func1():
    print("I am a function")


# Funtion that takes an argument
def func2(arg1, arg2):
    print(arg1, " ", arg2)


# Function that returns a value
def cube(x):
    return x * x * x


# Function with a default calue for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


# Function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


# func1()
# print(func1())
# print(func1)
func2(10, 20)
print(func2(10, 20))
print(cube(3))
print(power(2))
print(power(2, 3))
print(power(x=3, num=2))
print(multi_add(4, 5, 10, 4))
