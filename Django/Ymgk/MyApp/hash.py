import hashlib
import random



def hashIt(filepath):
    file = filepath# Location of the file (can be set a different way)
    BLOCK_SIZE = 65536 # The size of each read from the file

    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
      fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
      while len(fb) > 0: # While there is still data being read from the file
         file_hash.update(fb) # Update the hash
         fb = f.read(BLOCK_SIZE) # Read the next block from the file

    return (file_hash.hexdigest())

def populateHash(hash):
    for x in range(5, random.randint(10,20)):
        hash_object = hashlib.sha512(hash.encode())
        hash = hash + hash_object.hexdigest()
    return hash
