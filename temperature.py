#! /usr/bin/python

import sys
print ("Please Enter the Input of the temperature Unit:")

print ("")
FROM = input("Type 'C'(celsius)', 'F'(fahrenheit), 'K'(kelvin), 'R'(rankine) :").upper()
print(FROM)
if FROM == "C" or FROM == "F" or FROM == "K" or FROM == "R":
    print ("")
    VALUE = float(input(" Please Input the temperature in that unit :"))
    print("")
   
    if FROM == "C":
        kelvin = (VALUE + 273)
    elif FROM == "F":
        kelvin = ((5/9) * (VALUE - 32) + 273)
    elif FROM == "K":
        kelvin = VALUE
    elif FROM == "R":
        kelvin = (VALUE * (5/9))

else:
    print("")
    print ("Invalid temperature unit entered")
    sys.exit(1)
print ("")

TO = input("Please enter the desired temperature unit:\n Type 'C'(celsius)', 'F'(fahrenheit), 'K'(kelvin), 'R'(rankine) :").upper()
print("")
if TO == "C" or TO == "F" or TO == "K" or TO == "R":
    print ("")
    if TO == "C":
        END = (kelvin - 273)
    elif TO == "F":
        END = (1.8 * (kelvin - 273) + 32)
    elif TO == "K":
        END = kelvin
    elif TO == "R":
        END = (kelvin * (9/5))
else:
    print ("")
    print ("Invalid temperature unit entered")
    sys.exit(1)

expected = float(input("Please enter the input of student :"))
if (expected == END):
    print("Correct")
else:
    print("Incorrect")

print ("Your" ,  FROM , "value of" , VALUE , ", is" , END , "in" , TO )
