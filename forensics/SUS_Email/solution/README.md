# SUS Email

## Write-up

You can use any .eml file viewer to analyse the email, then you can notice two weird headers "Secret-Auth-Code" and "Security-Token".  
The payload in the token has a link to a pastbin, the password for the pastbin is the value of the Secret-Auth-Code.

## Flag

`shellmates{ceRtifIEd_eMAIL_4N4lY$1S_pRaCTiTi0N3r}`
