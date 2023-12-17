# Challenge name

## Write-up

The file contain logs for network traffic which seems filtered and extracted from a pcap file.
We can see that many **dns requests** are made to **dnsecret.shellmates.club**, but we can see clearly that the **record type** in every request is wrong like: `xtt, xxx, ttt...`.
But it looks like he is requesting for **txt record** from **dnsecret.shellmates.club**.
So all we have to make a **dns request** for **dnsecret.shellmates.club** asking for **txt record** to see what he was looking for. We can use tools like **nslookup** or **dig**
-> `dig txt dnsecret.shellmates.club`

## Flag

`shellmates{c2_s3RVER_mIgHt_UsE_TXt_R3c0RdS!!}`
