username = input("Username: ")
email = input("Email: ")

query_by_username = (
    "SELECT * FROM users WHERE username = %s",
    (username,)
)

query_by_email = (
    "SELECT * FROM users WHERE email = %s",
    (email,)
)

print(query_by_username)
print(query_by_email)
