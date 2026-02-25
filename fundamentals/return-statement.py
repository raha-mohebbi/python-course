#getting information back from a function
def cube(num):
   return num*num*num
print("code")

result = cube(4)
print(result) #64
# cube(3) #we are not getting anything back from the function, because we are not using the return statement
print(cube(3)) #None #return=> 27
#the return statement allows us to get a value back from a function, and we can use