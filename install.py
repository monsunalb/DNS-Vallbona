#!/usr/bin/python
# -*- coding: utf-8 -*-
#Desenvolupat per Albert Montaña

##########  A EDITAR  ###########

programlocation = "/home/albert/programs"	# A on voldràs el programa despres de la instalacio
						# (path completa "/home/...")

##########  ########  ###########

import os, sys, textwrap, time

def error(msg,exit):
	print(msg)
	if exit:
		print("exiting...")
		sys.exit()

def checkexixting(location):
	return os.path.isfile(location)

def checkroot():
	return os.geteuid()==0

def getinput(options):
	exit = 0
	maxm = len(options)
	for item in range(maxm):
		print (item+1,"-",options[item])
	while not exit:
		try: 
			value = int(input(">>"))
			if (1 <= value and value <= maxm):
				exit = 1
			else:
				print("Value has to be between %s and %s" %("1",str(maxm)))
		except ValueError: 
			print("Value has to be a number")
	return value

def message(msg):
	mesage = textwrap.wrap(msg, 42)
	print("\n  ##################################################")
	for item in mesage:
		print("  #   %s  "%item,end="")
		print(" "*(52-(len(item)+9))+"#")
	print("  ##################################################\n")

def editdoc(programlocation):
	with open("DNS.service","r") as doc:
		data = doc.readlines()
	data[5]="ExecStart=/usr/bin/python "+ programlocation+"\n"

	with open("DNS.service","w") as doc:
		doc.writelines(data)
	print(data)

def install():
	global programlocation

	if not os.path.exists(programlocation):
		to_pass = programlocation + " not found"
		error(to_pass,1)
	if not checkexixting("updatedns.py"):
		error("updatedns.py file and the installer have to be in the same folder",1)

	if not checkexixting("DNS.service"):
		error("DNS.service file and the installer have to be in the same folder",1)

	os.system("clear")
	to_pass = "Program path: "+programlocation
	message(to_pass)
	to_pass = "cp updatedns.py "+programlocation
	os.system(to_pass)
	editdoc(programlocation)
	os.system("cp DNS.service /etc/systemd/system")
	message("copy done")
	error("See you",1)

def edit():
	global programlocation
	programlocation=input("New full path\n>>")

def main():
	if not checkroot():
		error("Must be root",1)

	accio=getinput(["Start instalation","Edit program location","About","Exit"])
	if accio == 1:
		install()
	elif accio == 2:
		edit()
	elif accio == 3:
		message("This program is designed to avoid the DNS of institut Carles Vallbona 172.16.100.254")
		print("For any problem https://github.com/monsunalb/DNS-Vallbona/issues/new\n")
	elif accio == 4:
		error("See you",1)
	else:
		print("You hacked the program")

message("This program is offered with absolutely no warranties of proper working")
time.sleep(5)
while 1:
	main()