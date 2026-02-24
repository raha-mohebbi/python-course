# print ("Hello, World!")
character_name = "John"
character_age = "35"  #character_age = 35 
ismale = True   
print ("There once was a man named " + character_name + ", ")
print ("he was " + character_age + " years old. ")  #print ("he was " + str(character_age )+ " years old. ")      
character_name = "Mike"
print ("He really liked the name " + character_name + ", ")  
print ("Grraff \n academy")
phrase = "Giraffe Academy"
print (phrase + " is cool") #concatination
print (phrase.lower()) #lowercase function
print (phrase.upper()) #uppercase function
print (phrase.isupper()) #isupper function returns true if all characters are uppercase
print (phrase.upper().isupper()) #chaining functions
print(len(phrase)) #length function
print(phrase[0]) #indexing
print(phrase[3])
print(phrase[0:5]) #slicing     
print(phrase.index("G")) #index function returns the index of the first occurrence of the specified value
print(phrase.index("a"))     
print (phrase.replace("Giraffe", "Elephant")) #replace function replaces a specified value with another value