import math

# Reading the file
with open("the_wise_man.txt", 'r') as f:
    text = f.read()

# find the dimensions of the square matrix
length = len(text)
diagonal_length = int( math.sqrt(length) )

# iterating all diagonals
for count in range(diagonal_length):
    diagonal = ""
    i = count
    # iterating the elements of the selected diagonal
    for i in range(count, (length - count), (diagonal_length + 1)):
        diagonal += text[i]
    # testing if the flag exists in that diagonal
    if "shellmates" in diagonal:
        print(diagonal)
        break