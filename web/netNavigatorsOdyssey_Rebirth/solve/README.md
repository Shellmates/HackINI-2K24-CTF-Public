# Network Navigators Oddyssey: A Phoenix Rebirth
## Write-Up:
`shell=False` may prevent shell injections, but it won't make it immune against argument injection:
- If you go to "https://gtfobins.github.io/gtfobins/ip/" ( or checking `ip help` command ) you'll find that the `ip` binary may disclose file contents when used with `-force -batch $FILENAME` arguments.
- The `split()` method's default seperators are whitespaces (Spaces, TABs, and new lines), so even after blacklisting spaces, an attacker can still inject something like this:
```
-force
-batch
/flag.txt
```
(Use Shift+Enter to return to the line)
This input we be splitted based on new lines, and our subprocess function will look like this:
```
subprocess.check_output(['/sbin/ip', '-force', '-batch', '/flag.txt'], text=True,timeout=1,stderr=subprocess.STDOUT, shell=False)
```
which will still get evaluated as a valid command, an we will be able to read the flag or any other file we desire.
## Flag:
`shellmates{5laugh73r_7h3_Pho3niXx!___1njec7_1T_w1tH_@rgum3ntSs!!}`