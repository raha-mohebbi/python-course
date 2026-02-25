#functions are collections of code that perform a specific task and can be reused throughout a program
from os import name


def say_hello():
    print("hello user")
    # print("Top")
    say_hello()
# print ("Bottom")
#paramiter is a pice of a function that allows you to pass in a value when you call the function, and the function can use that value to perform its task
def say_hello(name): 
    print("hello " + name)
say_hello("Alice")

def say_hello(name, age):
    print("hello " + name + ", you are " + str(age) + " years old")
say_hello("Bob", 30)