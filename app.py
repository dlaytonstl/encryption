from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def encrypt_string(input_string, key):
    output = ""
    for char in input_string:
        if char in key:
            output += key[char]
        else:
            output += char
    return output

def decrypt_string(input_string, key):
    return encrypt_string(input_string, {v: k for k, v in key.items()})

@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html')

@app.route('/cipher', methods=['POST', 'GET'])
def cipher():
    key = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m",
           "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w",
           "u": "x", "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}

    if request.method == 'POST':
        input_string = request.form['input_string']
        action = request.form['action']

        if action == 'encrypt':
            result = encrypt_string(input_string.lower(), key)
            return render_template('cipher.html', cipher_result=result)
        elif action == 'decrypt':
            result = decrypt_string(input_string.lower(), key)
            return render_template('cipher.html', cipher_result=result)

    return render_template('cipher.html', cipher_result=None)

@app.route('/password_generator', methods=['GET', 'POST'])
def password_generator():
    special_characters = "!@#$%^&*()_-+=<>?/[]{}|"

    if request.method == 'POST':
        pass_len = int(request.form['pass_len'])
        if pass_len < 10 or pass_len > 20:
            return "Password length must be greater than 9"
        new_pass = ''
        for i in range(pass_len):
            add_character = random.choice([True, False])
            if add_character:
                random_numbers = random.randint(1, 10)
                new_pass += str(random_numbers)
                new_pass += str(random.choice(string.ascii_letters))
                new_pass += random.choice(special_characters)
            else:
                if len(new_pass) > 0:
                    random_index = random.randint(0, len(new_pass) + 3)
                    new_pass = new_pass[:random_index] + new_pass[random_index + 1:]
        return render_template('password_gen.html', password=new_pass)

    return render_template('password_gen.html', password=None)

if __name__ == '__main__':
    app.run(debug=True)


#worked

##OLD VERSION SHOULD ONLY BE USED FOR CONSOL
# from flask import Flask, render_template, request

# class MainApp:
#     def __init__(self, key: dict):
#         self.key = key
#         self.blank_string = ""
#         self.is_encrypting = True

#     def get_input(self) -> None:
#         to_do = input("What would you like to Encrypt or Decrypt your string?: ").strip().lower()
#         if to_do == 'encrypt':
#             self.is_encrypting = True
#             while True:
#                 blank_string = input("Enter a string to encrypt: ").strip().lower()
#                 if blank_string.isalpha():
#                     self.blank_string = blank_string
#                     break
#                 else:
#                     print('The input is not valid')
#         elif to_do == 'decrypt':
#             self.is_encrypting = False
#             while True:
#                 blank_string = input("Enter a string to decrypt: ").strip().lower()
#                 if blank_string.isalpha():
#                     self.blank_string = blank_string
#                     break
#                 else:
#                     print('The input is not valid')
#         else:
#             print('Invalid choice. Please choose "encrypt" or "decrypt"')

#     def encrypt_string(self) -> str:
#         output = ""
#         for i in self.blank_string:
#             for x, y in self.key.items():
#                 if i == x:
#                     output += y
#                 else:
#                     continue
#         return output

#     def decrypt_string(self) -> str:
#         decrypted_string = ""
#         for char in self.blank_string:
#             if char in self.key.values():
#                 for k, v in self.key.items():
#                     if v == char:
#                         decrypted_string += k
#             else:
#                 decrypted_string += char
#         return decrypted_string


# # Create a Flask app
# app = Flask(__name__)

# @app.route('/cipher', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         key = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m",
#                "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w",
#                "u": "x", "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}

#         main_app = MainApp(key=key)
#         main_app.blank_string = request.form['input_string']

#         if request.form['action'] == 'encrypt':
#             result = main_app.encrypt_string()
#         else:
#             result = main_app.decrypt_string()

#         return render_template('index.html', result=result)

#     return render_template('index.html', result=None)

# if __name__ == '__main__':
#     app.run(debug=True)