# OSCP-PREP
Useful scripts, resources for OSCP

- Crontab-list-jobs.sh

Description: List al the crontab jobs being executed. Makes a comparasion every second, so, you can easily spot the jobs that may require exploitation. 


- MacroGeneratorPayload.py

Description: Generate the entire payload for a Macro Word Document (just copy/paste).
Need to pass the payload (generated from https://www.revshells.com/) as argument. 



- SplitPayloadPS64.py 

Description: Splits the reverse shell payload (generated from https://www.revshells.com/) in blocks of 50 characters long.

- network-scan-bash.sh

Description: Scans a network range using bash. Usefull when you don't have nmap installed in a compromised machine

- port-scan-bash.sh

Description: Scans first 1000 ports for an IP Address using bash. Usefull when you don't have nmap installed in a compromised machine
Note: You can change the port range in the for loop. 

