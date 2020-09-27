#! /usr/bin/python3

print("Content-type: text/html")
print()

import os
import sys
import subprocess
import cgi 

command = cgi.FieldStorage()
value = command.getvalue('command')

flag = True

choice = value

if ('date' in choice.lower()):
	resultt = subprocess.getoutput('date')
	print(result)
	      
elif ('calender' in choice.lower())or('cal' in choice.lower()):
	result = subprocess.getoutput('cal')
	print(result)	
	
elif ('text' in choice.lower())or('notepad' in choice.lower()) or ('editor' in choice.lower()):
	result = subprocess.getoutput('sudo gedit')
	print(result)	
	
elif (('docker' in choice.lower())or('container' in choice.lower())) and ('start' in choice.lower() or 'launch' in choice.lower() or 'open' in choice.lower()):
	result = subprocess.getoutput('sudo systemctl start docker')

elif (('firewall' in choice.lower())or('firewalld' in choice.lower())) and ('start' in choice.lower() or 'launch' in choice.lower() or 'enable' in choice.lower()):
	result = subprocess.getoutput('sudo systemctl start firewalld')

else:
	print("Enter right command!")
