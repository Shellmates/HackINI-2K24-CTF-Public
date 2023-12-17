# matrix

## Write-up

- We have the file **the_wise_man.txt** that contains some data that looks random, the last sentence makes it clear that the flag is somehow hidden in that file.
The name of the challenge is **matrix**, we can understand that the file is considered as a matrix and its elements are the letters, which is exactly like the crosswords game.
The challenge also says **take it diagonally** which means that we are interested in the **diagonal words**.
- First we need to find the dimensions of the matrix so we can retrieve the caracters of the same diagonal word by counting the **root** of the length of the text ( there is a hint that the matrix is square )
- We have to iterate through the first 217 caracters ( each one of them is the first element of a diagonal word ), and in each iteration we have to read the caracters of that diagonal word, we can do that by iterating the caracters of the text starting from the number of the diagonal word we are in, to the end of the text with a `step = 217 + 1`
- Each time we get the diagonal word, we check if the string "shellmates" is in that word until we find the flag.
- We have to automate this process for sure: [solve](solve.py)

## Flag

`shellmates{YOu_vE_eaRnEd_w1$d0M_4ND_MaTH$Ss}`
