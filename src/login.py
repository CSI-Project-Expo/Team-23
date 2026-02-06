def login(username, password):
    if username == "admin" and password == "admin123":
        return True
    return False


if __name__ == "__main__":
    u = input("Username: ")
    p = input("Password: ")

    if login(u, p):
        print("Login successful")
    else:
        print("Login failed")
