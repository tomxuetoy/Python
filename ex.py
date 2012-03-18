### pickletest.py
### PICKLE AN OBJECT

# import the pickle module
import pickle

# lets create something to be pickled
# How about a list?
picklelist = ['one','two']

# now create a file
# replace filename with the file you want to create
file = open('filename', 'w')

# now let's pickle picklelist
pickle.dump(picklelist,file)

# close the file, and your pickling is complete
file.close()

# Running result:
# maemo@maemo-desktop:/mnt/hgfs/VMware_share/mycode/trial_python_fileIO$ python ex.py 
# maemo@maemo-desktop:/mnt/hgfs/VMware_share/mycode/trial_python_fileIO$ cat filename 
# (lp0
# S'one'
# p1
# aS'two'
# p2
# a.
