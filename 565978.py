import hashlib


def sha1_cracker(target_hash, character_set, password_length):
    import itertools

    for password_candidate in itertools.product(character_set, repeat=password_length):
        password = ''.join(password_candidate)
        print(password)
        hashed_password = hashlib.sha1(password.encode()).hexdigest()


        if hashed_password == target_hash:
            return password

    return None


# Відомий хеш SHA1
target_hash = 'aecf0292da85cb2048d8b648567127d024d4074f'

# Великі латинські літери
character_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Довжина пароля
password_length = 4

# Знайти шуканий пароль
found_password = sha1_cracker(target_hash, character_set, password_length)

if found_password:
    print('Знайдений пароль:', found_password)
else:
    print('Пароль не знайдений')