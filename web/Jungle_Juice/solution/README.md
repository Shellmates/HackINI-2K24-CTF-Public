# Jungle_Juice

## Write-up

We notice that there is an `==` operator instead of the strict one,which is a bad php practice. We will abuse this loose comparaison to bypass the check. We only need to give **choice=0e**, and **hash=PLtBEM6** to obtain the magic hash(we already have `1237` as a seed), et VOILA!!!

## Flag

`"shellmates{PHP_1$s$S$s$_W3EEEeEeEeeeEE3E33eEEE3EE33ee333e1Rd}"`