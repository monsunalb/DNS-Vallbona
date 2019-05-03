#!/usr/bin/python
import os,time

proceed = 0
llista = []
time.sleep(5)
fitxer = open("/etc/resolv.conf","r")
for item in fitxer.readlines():
	if item != "\n":
		print item.split()
		if item.split()[1] == "172.16.100.254":
			proceed = 1
		else:
			llista.append(item)
fitxer.close()

if proceed:
	print "s"
	fitxer = open("/etc/resolv.conf","w")
	for item in llista:
		fitxer.write(item)
	fitxer.close()