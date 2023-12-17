# Challenge name

## Write-up

since the attacker has penetrated the network , it is only logical to assume that he

tried to exfiltrate some documents in a stealthy way

you can notice that a host is requesting some DNS A records for a weird set of irregular subdomaines

that domaine is controlled by the attacked and he is sending the documents as byte streams inside the subdomaine part

so if you rearrange it , you find out the document that was exfiltrated is an image with our flag as content 

## Flag

`shellmates{DNS_3xfILtraT10n}`

