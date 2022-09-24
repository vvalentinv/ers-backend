import bcrypt


def hash_registering_password(passwd):
    return bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()


def validate_password(passwd, hash):
    print(hash)
    return bcrypt.checkpw(passwd.encode(), hash.encode())

