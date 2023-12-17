# Interrogation

## Write-up

- The challenge contains, as a hint: 
```bash
$ sudo -l
    ...
    User ctf may run the following commands:
    (Moriarty) /usr/bin/osqueryi
```
- Spawning an osquery shell as "Moriarty" and looking at different tables, here's an example of a solution: 
  
    1- The Tool:
        `SELECT * FROM file WHERE path LIKE '/usr/bin/%';`
    
    2- The group: 
        `.all groups`

    3- The server name:
        `.all crontab`


## Flag

`shellmates{Cr1m3m4st3rm1ndK1t_APT221_Th3Sh3rl0ck3d}`
