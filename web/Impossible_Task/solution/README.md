# Impossible Task

## Write-up

The solution for this challenge is in two steps:  
- The first step is to find a way to send body params although POST method is not allowed on the server, we can do this by sending body params with a GET request, this is called a fat GET request.
- The second step is to bypass the `.` restriction to send a request from the server to our server to get the flag, we also see that `%` is not allowed so we cannot bypass the restriction using URL-encoded characters. We can make use of the unidecode function to send a character like the Chinese dot `。` that will be decoded as a `.`.
Now we can send the URL to our server or webhook to get the flag.

## Flag

`shellmates{GETT1nG_FAT_w1Th_UN1C0DE_inj3CtiON}`
