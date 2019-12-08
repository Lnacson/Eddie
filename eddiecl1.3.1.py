#Copyright Tommy Ramsay & Nebulous inc. 2019 all rights reserved

import subprocess
import os

# variables
commands = ['say', 'drive', 'restart', 'shutdown', 'help', 'info', 'admin' ]
say = ""
adminPassword = "alpine"
adminAttempt = 0

version = "1.3.1 beta"

print("Welcome to Eddie Command-Line Version",version)
while True:
	print("------------------------------------------------")
	comm = input("\nInput Command: ")
	comm.lower()
	
	if comm not in commands:
		print("\nCommand not recognised, enter help for options. ")
	
	if comm == "say":
		while say != "exit()":

			say = input("Say: ")
			say.lower()
			if say != "exit()":
				subprocess.call(["say",say])
			
			
		print("\nSay command complete. ")
		
	
	if comm == "admin":
		while adminAttempt < 3:
			access = input("\nEnter admin password: ")
			access.lower()	
			if access == "alpine":
				adminAttempt = 3
				print("-----------------------------")
				print("\nWelcome to the admin pannel\n")
				
			adminAttempt +=1
		print("-----------------------------")
		print("\nExiting admin command...\n")
		
		
		
	if comm == "drive":
		comm = input("Launch Teleop? [y/n] ")
		if comm == "y":
			print("Launching Teleop In Paralell\n")
			os.system("roscore &")
			os.system("roslaunch turtlebot_bringup minimal.launch &")
			os.system("roslaunch turtlebot_teleop keyboard_teleop.launch")
			
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
	