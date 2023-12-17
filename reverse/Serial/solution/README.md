# First solution : Patching the binary
- What's first needed is to patch the call to the ```oh_no()``` function, replacing it with a ```nop```
- After that, the next instruction to be patched is ```__stack_chk_fail()``` in the ```generate_serial()``` function, replacing it also with a ```nop```
- After that supplying the string 'reverse_practitioner' to the program will give the needed serial
- It can be easily done using Ghidra

# Second solution : Calculating the serial
- The serial is calculated as follows
- It considers only the first 12 characters, and the length of the given string
- Those 12 characters are divied to 3 chunks of 4 characters each
- The ASCII values of the characters of a chunk are summed, and then we add the total sum of all the string's characters
- The result is a string of the following form : XXXX-XXXX-XXXX
- After constructing the program, we give it the string 'reverse_practitioner'