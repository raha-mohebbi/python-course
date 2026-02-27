#allows us to perform mathematical operations on numbers, such as addition, subtraction, multiplication, and division
#2d lists are lists that contain other lists as elements, and nested loops are loops that are contained within other loops, which can be used to iterate through the elements of a 2d list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print (number_grid[2][1]) #prints the first element of the first list, which is 1. first row first column
print (number_grid[0][1]) #prints the second element of the first list,
for row in number_grid: #for every row in the number grid do the following
    print(row)
for row in number_grid: #for every row in the number grid do the following
    for col in row: #for every column in the row do the following
        print(col) #print the column