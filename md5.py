print "ONLY FOR ILLEAGLE PURPOSE!\n" 

import md5

counter = 1

pass_in = raw_input("please enter the hash")
pwfile = raw_input("Pass file name:")

try:

	pwfile = open(pwfile, "r")
except:
	print "\nFilenot found."
	quit()

for password in pwfile:
	filemd5 = md5.new(password.strip()).hexdigest()
	print "trying pass number %d: %s " % (counter, password.strip())

	counter += 1

	if pass_in == filemd5:
		print "\nmatch found. \npassword is: %s" % password
	 	break

else: print "\npass not found"
