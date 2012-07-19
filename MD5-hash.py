import hashlib

input_string = raw_input() # added by Tom Xue
m = hashlib.md5()
m.update(input_string)

print m.digest()
print m.hexdigest() 
