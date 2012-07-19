#!/usr/bin/env python
# All comments start with a the character "#"
# This program converts human years to dog years
# get the original age
age = input("Enter your age (in human years): ")
print # print a blank line
# check if the age is valid using a simple if statement
if age < 0:
	print "A negative age is not possible."
elif age < 3 or age > 110:
	print "Frankly, I don't believe you."
else:
	print "That's the same as a", age/7, "year old dog."
