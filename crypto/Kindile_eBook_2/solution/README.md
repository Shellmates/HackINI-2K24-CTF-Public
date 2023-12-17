# Challenge name
Kindile_eBook_2
## Write-up
- I guess at this point you should know the scholar referred to in the description and in the name of the challenge is Al-Kindi, he is the one who came up with the first technique of cryptanalysis, we'll explain the method in this solution (it's also explained in the original text).

- It is about knowing the frequency distribution (or the percentages of occurrences) of a language's characters and then comparing them to the occurrences of the characters we have in our text, we get the original ones by simply matching.

- In our case it will be as follows:

	E	12.60 %		#	12.08%
	T	9.37 %		]	8.94%
	A	8.34 %		1	7.19%
	O	7.70 %		+	6.64%
	N	6.80 %		~	6.56%
	I	6.71 %		[	6.52%
	H	6.11 %		&	6.08%
	S	6.11 %		|	5.41%
	R	5.68 %		^	4.57%
	L	4.24 %		)	4.49%
	D	4.14 %		!	4.33%
	U	2.85 %		@	3.22%
	C	2.73 %		_	2.50%
	M	2.53 %		?	2.38%
	W	2.34 %		/	2.34%
	Y	2.04 %		%	2.19%
	F	2.03 %		$	2.15%
	G	1.92 %		{	2.11%

- We start replacing characters and see more recognizable words, there are some that are close in the percentages so we need to try the cases and see if it's the correct one.
	 

## Flag

`shellmates{CryptanalysisCanDoSoooMuch}`
