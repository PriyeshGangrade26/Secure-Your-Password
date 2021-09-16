SECURE = (('s', '$'), ('and', '&'), 
            ('a', '@'), ('o', '0'), ('i', '!'),
            ('I', '|'), ('h', '#'), ('g', '9'), ('P', '%'), ('1', 'I'), ('2', 'S'), ('3', 'E'))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a, b)
    return password

if __name__ == "__main__":
    password = input("Enter your password: \n")
    password = securePassword(password)
    print(f"Your secure password is {password}")