# Traffic Engineering

## Write-up

From the desciption we can understand that the challenge has to do with wireless communications and protocols but we don't know what is it exacly.  

We have two files, let's take a look at the pcap file, when we open the file with **wireshark**, we can see that it contains regular traffic like HTTPS, DNS and ICMP.  
Looking closely at the **ICMP** packets we can notice weird data sizes in some packets, we can think of a **data exfiltration** technique using pings, decoding that to data to ascii will give us the following message: `ping data exfiltration, here is the password, you will need it later: 1234567890`.  
This can be done manually or using tools like **Tshark** or **scapy** (for python).  
Now that we have a password, let's take a look at the second file.The file doesn't have any extension and the "file" command does give much infomation about it.
As the description says , the ile is corrupted and we must recover it.For that we can use a tool called **pcapfix** (You can find it on github : https://github.com/Rup0rt/pcapfix),or we can just open it and notice that the first 4 bytes of the file are just 00 00 00 00 so we look for PcapNG files which  is **0a 0d 0d 0a** and we just add it.
Now that we opened the file we can see traffic for **802.11** protocol commonly know as WIFI, so maybe the password is for authentication to a WIFI network, to decrypt the trafficwe can guess that it is using WPA/WPA2, so we must get the SSID ,we can see an SSID called `Xd` in the WIFI frames, now we can add the to the IEEE 802.11 keys `1234567890:Xd` to create a pre-shared WPA key.  
Now we can see decrypted traffic that contains some http requests containing the flag. 
## Flag

`shellmates{wp4_h3cker_4nd_traffic_eng1ne3ring}`
