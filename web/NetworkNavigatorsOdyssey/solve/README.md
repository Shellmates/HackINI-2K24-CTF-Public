# Network Navigators Oddyssey Writeup
## The Weaknesses
### Command Injection:
- User input is being passed directly to `subprocess.Popen()` function with `shell=True`, which allows it to be interpreted by the system shell.
### Whitelist Bypass:
- Enter a random value as an option and you'll get the following error:
```
Sorry, but only these options are availabe: ['address', 'link', 'maddress', 'neighbor', 'netconf', 'ntable', 'route', 'rule', 'tcpmetrics', 'token']
```

- If you look closely at the code, you'll spot that the code doesn't check if the option is completely equal to one of the options in the whitelist, but only checks whether it's present there or not, so an attacker could simply enter `testaddress` , and he won't get and error, because `address` is whitelisted.
### Blacklist bypass:
Implementing a blacklist to prevent command injection might not be the most effective approach. In this case, the developer forgot the pipe symbol `|` which leaves the attacker with the ability to execute system commands on the server using something like `||id||address` .
## Reading the flag
- Now that we have RCE, we can try something like `||ls${IFS}/||address` to locate the flag ( `${IFS}` is used to bypass blacklisted whitespaces), you'll get something like this in the output : 
```
app
bin
dev
etc
flagfbbed20a24.txt
home
.
.
.
```
Finally, you can read it using `||grep${IFS}"shellmates"${IFS}/flag*||address` (PS : you may find another solution to do it)

## Flag
`shellmates{S1l3nc3d_S3rv3r5___Ech0_Just1c3}`