import random

chars = 'aАbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTvVwWxXyYzZ1234567890_$%#'
n = int(input('Enter password length: '))
password = ''

if n >= 8 and n <= 16:
    for x in range(n):
        password += random.choice(chars)
    print(password)
elif n <= 8:
    print('The password must be at least 8 characters')
elif n >= 16:
    print('The password can contain up to 16 characters')