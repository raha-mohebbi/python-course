#type of a data structure that is immutable (cannot be changed after creation)
#tuples are ordered collection of items
#basically means a container where you can store the values but you cannot change them
coordinates = (4, 5) #inside the perenthese we have the values that we want to store in the tuple, and we separate them with a comma
print(coordinates[0]) #4
print(coordinates[1]) #5
#lists : can be changed or assigned new values, but tuples cannot be changed or assigned new values
#tuples are faster than lists because they are immutable, and they use less memory than lists
coordinates=[(4, 5), (6, 7), (8, 9)] #we can have a list of tuples, which is a common way to store data in Python
print(coordinates) #[(4, 5), (6, 7), (8, 9)]