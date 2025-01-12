import random

def get_user_choice():
    user_input = input("انتخاب خود را وارد کنید (سنگ، کاغذ، قیچی): ")
    while user_input not in ["سنگ", "کاغذ", "قیچی"]:
        print("انتخاب نامعتبر است. لطفاً دوباره تلاش کنید.")
        user_input = input("انتخاب خود را وارد کنید (سنگ، کاغذ، قیچی): ")
    return user_input

def get_computer_choice():
    return random.choice(["سنگ", "کاغذ", "قیچی"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "مساوی!"
    elif (user_choice == "سنگ" and computer_choice == "قیچی") or \
         (user_choice == "کاغذ" and computer_choice == "سنگ") or \
         (user_choice == "قیچی" and computer_choice == "کاغذ"):
        return "شما برنده شدید!"
    else:
        return "کامپیوتر برنده شد!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"شما انتخاب کردید: {user_choice}")
    print(f"کامپیوتر انتخاب کرد: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
