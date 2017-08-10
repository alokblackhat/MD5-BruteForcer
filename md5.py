print "ONLY FOR LEGAL PURPOSE!\n" 

import md5

counter = 1

pass_in = raw_input("PLEASE ENTER YOUR MD5 HASH:")
pwfile = raw_input("PATH TO YOUR BRUTE-FORCE DICTIONARY:")

try:

	pwfile = open(pwfile, "r")
except:
	print "\nFilenot found."
	quit()

for password in pwfile:
	filemd5 = md5.new(password.strip()).hexdigest()
	print "TRYING PASSWORD NUMBER %d: %s " % (counter, password.strip())

	counter += 1

	if pass_in == filemd5:
		print "\nPASSWORD CRACKED. \nPASSWORD IS: %s" % password
	 	break

else: print "\nPASSWORD NOT FOUND!"
