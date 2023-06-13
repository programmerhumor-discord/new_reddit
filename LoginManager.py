import hashlib

def makeSHA(s):
    return hashlib.sha256(s.encode()).hexdigest()

def confirmLogin(email, password):
    print("Implement this!")
    return [True, "username"]

def createLogin(email, password):
    with open("user.data", "w") as f:
        # email
        # password (sha256)
        f.writeLines([email, makeSHA(password)])

def checkLogin():
    email, password = "", ""
    try:
        with open("user.data", "r") as f:
            email, password = f.readlines()
            email, password = email.split("\n")[0], password.split("\n")[0]
    except:
        return [False]
    res, username = confirmLogin(email, password)
    return [res, email, password, username]
