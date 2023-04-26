import hashlib

email = "antar@gmail.com"
pwd = "ChairOnTableWith3Legs"
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

your_email = "antar@gmail.com"
your_password = "ChairOnTableWith3Legs"

heashed_your_password = hashlib.md5(your_password.encode()).hexdigest()

if email == your_email and pwd_hash == heashed_your_password:
    print("Right user")

hacker_email = "antar@gmail.com"
hacker_password = "2329e22c9a4de221abeabaf22b72c7fc"

if email == hacker_email and pwd_hash == hacker_password:
    print("Wrong password")

print(pwd)
print(pwd_hash)