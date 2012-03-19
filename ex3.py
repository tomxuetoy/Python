# Let's create a file and write it to disk.
filename = "test.dat"
# Let's create some data:
namelist = []
while True:
    name = raw_input("Enter a name:")
    if name:
	    namelist.append(name)
    else:
	    break

# Create a file object:
# in "write" mode
FILE = open(filename,"w")

# Write all the lines at once:
FILE.writelines(namelist)
    
# Alternatively write them one by one:
for name in namelist:
    FILE.write(name)
    
FILE.close()
