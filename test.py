import hashlib


i = "admin".encode()

hash = hashlib.md5(i)

print(hash.hexdigest())
