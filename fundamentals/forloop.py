for letter in "Giraffe Academy": #for in every letter in the string "Giraffe Academy" do the following
    print(letter)
friends = ["Jim", "Karen", "Kevin"]
for friend in friends: #for every friend in the list of friends do the following
    print(friend)

    for index in  range (len(friends)): #for every index in the range of the length of the list of friends do the following
        print(friends[index])
        friends[2]

        for index in range(5): #for every index in the range of 5 do the following
           if index == 0:
               print("first iteration")
           else:
               print("not first")