import hashlib

test_value = "workflow-verification"
test_hash = hashlib.md5(test_value.encode())

print(test_hash.hexdigest())
