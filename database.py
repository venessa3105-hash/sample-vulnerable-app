username = input("Username: ")

query = "SELECT * FROM users WHERE username='" + username + "'"
query = (
    "SELECT * FROM users "
    "WHERE email='"
    + email
    + "'"
)

print(query)
