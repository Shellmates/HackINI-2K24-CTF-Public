
# Pathfinder2

## Write-up

This time there is a huge blacklist, and the 1st thing we notice is that **{{ }}** are blocked, after some research, we can find that **{%** can replace it, but there is one problem, we can execute commands but we cannot see the input, so we have a blind SSTI. We can use some useful functions like **|attr** to bypass some blacklisted characters, we can use hexa encoding too, then we are left with the command execution,we can use something like **'if head flag* | grep -q "shellmates{"; then sleep 5; fi'** then brute force all the other characters.

## Flag

`shellmates{yoUUUUu_aReeEeeEE_NOOWww_OfFfFFFIciAlLyyYY_MYyyYYy_besToOo0000OO0o_FrieEEeeEEnddoOOOoOo}`