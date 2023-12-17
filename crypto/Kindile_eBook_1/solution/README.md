# Challenge name
Kindile_eBook_1
## Write-up
- There are different ways to solve this challenge. I'll explain one of them here, you can find another one as the solution of the second challenge.

- From the challenge description we know we have a text extracted from a book, but it is ciphered in some way, we need to get the original text. 

- We can manually (or by using a tool/script) deduce the original letters from the ciphered ones and that's by using common and repetitive words and their probable match.

- Here is an example:
	"boeb" is repetitive in our ciphered text, it starts and ends with the same letter, so considering english, it could be a "that", which means b=t, o=h, e=a
	
- By replacing the letters we find, we start recongnizing more and more words. 

## Flag

`shellmates{JustASimpleAnalysis}`
