import random
import string 

def pass_gen():
    special_characters = "!@#$%^&*()_-+=<>?/[]{}|"

    pass_len = int(input("Enter how long you want the password to be (Must be at least 10): "))
    if pass_len < 10:
        print("The password must be greater than 9")
    else:
        new_pass = ''
        for i in range(pass_len):
            add_character = random.choice([True, False])
            if add_character:
                random_numbers = random.randint(1,10)
                new_pass += str(random_numbers)
                new_pass += str(random.choice(string.ascii_letters))
                new_pass += random.choice(special_characters)
            else:
                random_index = random.randint(1, len(new_pass) - 1)
                new_pass = new_pass[:random_index] + new_pass[random_index + 1:]
        print(new_pass)