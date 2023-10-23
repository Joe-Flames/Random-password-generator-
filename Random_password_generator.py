import random

def generate_random_password():
    password_length = random.randint(7, 10)
    password = ''.join(chr(random.randint(33, 126)) for _ in range(password_length))
    return password

if __name__ == "__main__":
    random_password = generate_random_password()
    print("Randomly generated password:", random_password)
