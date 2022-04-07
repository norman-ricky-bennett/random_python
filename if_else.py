#! /usr/bin/python3

a = input("Please enter the port you would like to scan: ")

if int(a)<70000:
	print("Scanning...")

else:
	print("Invalid port number; please enter a new number: ")