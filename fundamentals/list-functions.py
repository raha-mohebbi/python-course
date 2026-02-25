lucky_numbera=[3, 7, 13, 42, 16]
friends = ["Alice", "Bob", "Charlie", "David", 2]
#extension functions: allow you to take a list and append  another list onto the end of it
friends.extend(lucky_numbera)
friends.append("Eve") #append function: allows you to add a single item to the end of a list
friends.insert(0, "Zara") #insert function: allows you to add a single item at a specific index in a list. the first parameter is the index where you want to insert the item, and the second parameter is the item itself
friends.remove("Bob") #remove function: allows you to remove a specific item from a list. if the item is not found in the list, it will raise a ValueError
friends.pop() #pop function: allows you to remove and return the last item from a list
friends.clear() #clear function: allows you to remove all items from a list, leaving it empty
print(friends.index("Charlie")) #index function: allows you to find the index of a specific item in a list. if the item is not found in the list, it will raise a ValueError
print(friends.count("Alice")) #count function: allows you to count the number of occurrences of a specific item in a list
friends.sort() #sort function: allows you to sort the items in a list in ascending order. if the list contains items of different types, it will raise a TypeError
lucky_numbera.reverse() #reverse function: allows you to reverse the order of the items in a list
print(friends)