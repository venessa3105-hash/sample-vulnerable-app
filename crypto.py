import hashlib

password = "admin"

hash_value = hashlib.md5(password.encode())

print(hash_value.hexdigest())
