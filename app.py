import secrets
import string
import time


strong_password_length = 15


def welcome_banner():
    print("*" * 20)
    print("Password Generator")
    print("by Euvrein")
    print("*" * 20)
    print("")


def menu():
    while True:
        print('''Here are your choices:
            \rC) Check Password Strength
            \rG) Generate Password
            \rQ) Quit the Application
        ''')
        choice = input('\n> ')
        choice = choice.upper()
        if choice in ['C', 'G', 'Q']:
            return choice
        else:
            input('''
            \rPlease choose one of the options (C, G, or Q)
            \rPress enter to try again.''')


def generate_password():
   letters = string.ascii_letters
   digits = string.digits
   special_chars = string.punctuation

   characters = letters.upper() + letters.lower() + digits + special_chars
   password = ''
   password_strong = False

   while not password_strong:
       password = ''
       for i in range(strong_password_length):
           password += ''.join(secrets.choice(characters))

       if (any(char in special_chars for char in password) and
               sum(char in digits for char in password) >= 2):
           password_strong = True

   return password


def check_password_strength():
    password = input('Enter the password: ')
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1
    if len(password) >= strong_password_length:
        strength += 1

    if strength == 1:
        remarks = 'Very Weak'
    elif strength == 2:
       remarks = 'Weak'
    elif strength == 3:
        remarks = 'Good'
    elif strength == 4:
        remarks = 'Strong'
    elif strength == 5:
        remarks = 'Very Strong'

    print('Your password has:-')
    print(f'{lower_count} lowercase letters')
    print(f'{upper_count} uppercase letters')
    print(f'{num_count} digits')
    print(f'{special_count} special characters')
    print(f'{len(password)} password length')
    print(f'Password Score: {strength / 5}')
    print(f'Remarks: Password is {remarks}')


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == 'C':
            check_password_strength()
            pass
        elif choice == 'G':
            print("Generating password...\n")
            time.sleep(1)
            generated_password = generate_password()
            print(f"Generated Password: {generated_password}")
        else:
            print('Closing App. Thank you for using this App!')
            app_running = False

        input("\nPress enter to return to the main menu")


if __name__ == '__main__':
    welcome_banner()
    app()



