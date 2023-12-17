# Writeup
First of all we need to search about the techniques used by APT41 (Advanced Persistant Threat 41) for web servers remote control, we will find that they use web shells [link](https://attack.mitre.org/groups/G0096/).  
If we search for the following key words "APT41 web shell php", we will find a web shell called China Chopper: [link1](https://attack.mitre.org/software/S0020/),[link2](https://attack.mitre.org/techniques/T1505/003/)  
We can then make a yara rule to find the malicious file (check rule.yara file).  
Here is how to use this yara rule on windows: yara64.exe rule.yara uploads  

This is not the only solution but yara rules are widely used in the context of malware detection.  
- the flag is: shellmates{1241-China-Chopper}