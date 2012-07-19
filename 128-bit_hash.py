import random

# A md5-hash is just a 128-bit value
hash = random.getrandbits(128)

print "hash value: %032x" % hash
