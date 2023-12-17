# jail

## Write-up

in this challenge of jail, I added 2 things: 
1- in the last of the code you can see that I delete 9 chars from the path if it was correct so it doesn't let you put it correctly until you add 9 chars after the real path
2- I added lseek function which moves  the offset of the file which we are reading.so to put it on the 1st char you should put the number 0 from on of the folder 0ne_Sh0t
    in the path number exactly, so you should calculate the place, you enter to a file than you go out until you put it in it.
3-payload : ../Tooo0Cl0se/../9indil/flag/flag/fla
## Flag

`shellmates{G0oD_J0b_B1g_Sm0k3}`
