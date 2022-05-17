#!/usr/bin/python

#Insert your payload Based64 below: Format <powershell.exe -nop -w hidden -e CODE>
payload = ' ' 

n = 50
for i in range(0, len(payload), n):
    print "Str = Str + " + '"' + str[i:i+n] + '"'
