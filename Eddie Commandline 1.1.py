#Copyright Tommy Ramsay & Nebulous inc. 2020 all rights reserved

import subprocess

commands = ['say', 'drive', 'restart', 'shutdown', 'help', 'info' ]
say = ""

print("Welcome To Eddie")
while True:
	print("----------------")
	comm = input("\nInput Command: ")
	comm.lower()
	
	if comm not in commands:
		print("\nCommand not recognised, enter help for options. ")
	
	if comm == "say":
		while say != "exit()":

			say = input("Say: ")
			say.lower()
			subprocess.call(["say",say])
			
		print("\nSay command complete. ")
		
		
	if comm == "drive":
		comm = input("Launch Teleop? [y/n] ")
		if comm == "y":
			print("Launching Teleop In Paralell")
			#teleop command here
			
	if comm == "restart":
		print("\nRestarting now")
		#restart command
		
	if comm == "shutdown":
		print("\nShutting down...")
		exit()
	
	if comm == "help":
		print("""Command Options:
- Say Command
- Help Command
- Drive Command
- Restart Command
- Shutdown Command""")

	if comm == "info":
		print("""
Please enter a Command you would like information about:
- Say 
- Help 
- Drive 
- Restart 
- Shutdown 
- Exit""")
		information = input("\nEnter here: ")
		information.lower()
		while information != "exit":

			if information not in commands:
				print("\nInvalid response. ")
				information == "exit"

			if information == "say":
				print("\nThe Say command takes the user's input and speaks it aloud. ")
				information == "exit"

			if information == "drive":
				print("\nThe Drive command allows the user to control this Robot's movement with a keyboard. ")
				information == "exit"

			if information == "restart":
				print("\nThe Restart command restarts the Robot - allowing a fresh start. ")
				information == "exit"

			if information == "shutdown":
				print("\nThe Shutdown command... well... it's pretty self-explanatory. ")
				information == "exit"
			
		print("\nExiting info Command. ")
	