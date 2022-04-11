#! /usr/bin/python3

fname = input("Please enter the file you would like to search: ")

searchFor = input("Please enter the keyword you would like to search: ")

fhand = open(fname)

for line in fhand:
	if line.startswith(searchFor):
		count = count + 1

print("There ")

