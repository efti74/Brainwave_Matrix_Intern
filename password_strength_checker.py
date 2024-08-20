from zxcvbn import zxcvbn
import pyfiglet

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '[', ']', '{ ', '}', '|', '\\', ';', ':', '\'', '\"', '<', '>', ',', '.', '?', '/']

def check_password_strength(password):
    result = zxcvbn(password)
    
    print(f"🔒 Password: {result['password']}")
    print(f"📊 Score: {result['score']}/4")
    print(f"⏰ Estimated time to crack: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
    print(f"💡 Feedback: {result['feedback']['suggestions']}")

def rate_password_by_strength_point(strength):
    if strength == 5:
        print("🔒 Password is strong 💪")
    elif strength == 4:
        print("👍 Password is good 👌")
    elif strength == 3:
        print("🤔 Password is fair 🤝")
    elif strength == 2:
        print("😬 Password is weak 😔")
    elif strength == 1:
        print("😱 Password is very weak 😳")

def rate_password_by_using_point(digitUsed, lowerUsed, upperUsed, moreThan8, specialUsed):
    if digitUsed is False:
        print("🚫 Password does not contain any digit")
    elif lowerUsed is False:
        print("🚫 Password does not contain any lowercase letter")
    elif upperUsed is False:
        print("🚫 Password does not contain any uppercase letter")
    elif moreThan8 is False:
        print("🚫 The length is very short for the strong password")
    elif specialUsed is False:
        print("🚫 Password does not contain any special character")

def check_password_policy(password):
    strength = 0
    digitUsed = False
    lowerUsed = False
    upperUsed = False
    moreThan8 = False
    specialUsed = False
    for  char in password:
        if char.isdigit() is True and digitUsed is not True:
            strength += 1
            digitUsed = True
        elif char.islower() is True and lowerUsed is not True:
            strength += 1
            lowerUsed = True
        elif char.isupper() is True and upperUsed is not True:
            strength += 1
            upperUsed = True
        elif len(password) >= 8 and moreThan8 is not True:
            strength += 1
            moreThan8 = True
        elif char in special_characters and specialUsed is not True:
            strength += 1
            specialUsed = True

    rate_password_by_strength_point(strength)

    rate_password_by_using_point(digitUsed, lowerUsed, upperUsed, moreThan8, specialUsed)

    check_password_strength(password)

def welcome_note():
    f = pyfiglet.Figlet(font='cybermedium')
    print(f.renderText('PASSWORD CHECKER'))
    print("👋 This program will help you fortify your online security by analyzing your password's strength and providing personalized recommendations to protect your digital identity.\n")

def main():
    welcome_note()
    password = input("🔑 Enter your password: ")
    check_password_policy(password)


if __name__ == "__main__":
    main()