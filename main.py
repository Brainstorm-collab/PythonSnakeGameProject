# # # ---------------------------------------------- Timer Program ⏳ -----------------------------------------------------------------------
# # import time
# # my_time = int(input("Enter the time: "))
# # for i in reversed(range(my_time)):
# #     seconds = i % 60
# #     time.sleep(1)
# #     print(f'Time is 00:00:{seconds:02}')
# # print("⏰ Time's up!")
# # from os import write
# #
# # # # --------------------------------- Food Item Cart Program 🛒 -------------------------------------------------------------------------------------------------------------------
# # # foods = []
# # # prices = []
# # # total = 0
# # #
# # # while True:
# # #     food = input("Enter the food items [type 'q' if done with selecting]: ")
# # #     if food == 'q':
# # #         break
# # #     else:
# # #         price = int(input(f"Enter the price of {food} in rupees: "))
# # #         foods.append(food)
# # #         prices.append(price)
# # #
# # # print("\n----------- YOUR CART ----------")
# # # for food in foods:
# # #     print(food, end=' ')
# # # print()
# # #
# # # total = sum(prices)
# # # print(f"💰 The total price to pay is {total} rupees")
# # #
# # # ----------------------------------------------- MCQ Program 🎓 ----------------------------------------------------------------------------------------
# # # questions = (
# # #     "What is the capital of India?",
# # #     "Who is known as the Father of the Nation in India?",
# # #     "Which planet is known as the Red Planet?",
# # #     "What is the largest mammal in the world?"
# # # )
# # #
# # # options = (
# # #     ("a. Mumbai", "b. Kolkata", "c. New Delhi", "d. Chennai"),
# # #     ("a. Jawaharlal Nehru", "b. Mahatma Gandhi", "c. Subhas Chandra Bose", "d. Bhagat Singh"),
# # #     ("a. Venus", "b. Mars", "c. Earth", "d. Saturn"),
# # #     ("a. Horse", "b. Whale", "c. Peacock", "d. Kangaroo")
# # # )
# # #
# # # answers = ("c", "b", "b", "b")
# # # guesses = []
# # # score = 0
# # # question_num = 0
# # #
# # # for question in questions:
# # #     print("---------------------------------------------------------------------------------------------------------")
# # #     print(question)
# # #     for option in options[question_num]:
# # #         print(option)
# # #
# # #     guess = input("Enter your answer (a/b/c/d): ").lower()
# # #     guesses.append(guess)
# # #
# # #     if guess == answers[question_num]:
# # #         print("✅ Correct!")
# # #         score += 1
# # #     else:
# # #         print(f"❌ Wrong! The correct answer is {answers[question_num]}.")
# # #
# # #     question_num += 1
# # #
# # # print("-------------------------------------------------------------------------------------------------------------")
# # # print("                                    📊 RESULTS                                                                  ")
# # # print("-------------------------------------------------------------------------------------------------------------")
# # # print("Correct Answers:   ", " ".join(answers))
# # # print("Your Answers:      ", " ".join(guesses))
# # #
# # # percentage_score = int((score / len(questions)) * 100)
# # # print(f"🏆 Your final score is: {percentage_score}%")
# # # #
# # # # --------------------------------- Menu Card Program 🍽️ ----------------------------------------------------------------------------------------------------
# # # menu = {
# # #     "popcorn": 300,
# # #     "coke": 100,
# # #     "sandwich": 60,
# # # }
# # #
# # # total = 0
# # # cart = []
# # # print("--------- MENU ----------")
# # # for key, value in menu.items():
# # #     print(f"{key:10}: {value:.2f}")
# # # print("-----------------------")
# # #
# # # while True:
# # #     food = input("Select the items from menu (press 'q' to quit): ").lower()
# # #     if food == "q":
# # #         break
# # #     elif food in menu:
# # #         cart.append(food)
# # #
# # # print("------- YOUR ORDER -------")
# # # for food in cart:
# # #     total += menu[food]
# # #     print(food, end=' ')
# # # print()
# # # print(f'💰 Your total is {total:.2f}')
# # # print("-----------------------")
# # #
# # # # # ----------------------------------------- Random Number Game 🎲 ---------------------------------------------------------------------------------
# # # import random
# # #
# # # low = 1
# # # high = 100
# # # answer = random.randint(low, high)
# # # guesses = 0
# # #
# # # print("--------------- WELCOME TO NUMBER GUESSING GAME 🎯 ------------------")
# # # print(f"SELECT A NUMBER BETWEEN {low} AND {high}")
# # #
# # # while True:
# # #     guess = input("ENTER YOUR GUESS: ").strip()
# # #
# # #     if not guess.isdigit():
# # #         print("⚠️ INVALID GUESS. Please enter a number.")
# # #         continue
# # #
# # #     guess = int(guess)
# # #
# # #     if guess < low or guess > high:
# # #         print(f"⚠️ INVALID GUESS. Make sure your guess is between {low} and {high}.")
# # #         continue
# # #
# # #     guesses += 1
# # #
# # #     if guess == answer:
# # #         print(f"🎉 CONGRATULATIONS! You guessed the number in {guesses} {'try' if guesses == 1 else 'tries'}! 🎉")
# # #         break
# # #     elif guess < answer:
# # #         print("⬆️ Too low! Try a higher number.")
# # #     else:
# # #         print("⬇️ Too high! Try a lower number.")
# # # -------------------------------------------ROCK PAPER SCISSOR GAME--------------------------------------------------------------------------
# # # import random
# # #
# # # is_running = True
# # # options = ("Rock", "Paper", "Scissor")
# # #
# # # while is_running:
# # #     computer = random.choice(options).capitalize()
# # #     your = None
# # #
# # #     while your not in options:
# # #         your = input("Select (Rock ✊ / Paper 🤚 / Scissor ✌️): ").capitalize()
# # #
# # #         print(f"Computer's Choice: {computer} 💻")
# # #         print(f"Your Choice: {your} 🚀")
# # #
# # #         if your == computer:
# # #             print("That's a Tie! ⚖️")
# # #         elif your == "Scissor" and computer == "Paper":
# # #             print("You Won! 🎉")
# # #         elif your == "Paper" and computer == "Rock":
# # #             print("You Won! 🎉")
# # #         elif your == "Rock" and computer == "Scissor":
# # #             print("You Won! 🎉")
# # #         else:
# # #             print("Computer Won! 💪")
# # #
# # #         play_again = input("Wanna Play Again? (Y/N) 🚀: ").upper()
# # #         if not play_again == "Y":
# # #             is_running = False
# # #-------------------------------------------------------DICE ROLLER PROGRAM_________________________________________________________________
# # # import random
# # #
# # # dice_art = {
# # #     1: ("┌─────────┐",
# # #         "│         │",
# # #         "│    ●    │",
# # #         "│         │",
# # #         "└─────────┘"),
# # #     2: ("┌─────────┐",
# # #         "│  ●      │",
# # #         "│         │",
# # #         "│      ●  │",
# # #         "└─────────┘"),
# # #     3: ("┌─────────┐",
# # #         "│  ●      │",
# # #         "│    ●    │",
# # #         "│      ●  │",
# # #         "└─────────┘"),
# # #     4: ("┌─────────┐",
# # #         "│  ●   ●  │",
# # #         "│         │",
# # #         "│  ●   ●  │",
# # #         "└─────────┘"),
# # #     5: ("┌─────────┐",
# # #         "│  ●   ●  │",
# # #         "│    ●    │",
# # #         "│  ●   ●  │",
# # #         "└─────────┘"),
# # #     6: ("┌─────────┐",
# # #         "│  ●   ●  │",
# # #         "│  ●   ●  │",
# # #         "│  ●   ●  │",
# # #         "└─────────┘")
# # # }
# # #
# # # dice = []
# # # total = 0
# # # num_of_dice = int(input("How many dice?: "))
# # #
# # # for die in range(num_of_dice):
# # #     dice.append(random.randint(1, 6))
# # #
# # # # PRINT VERTICALLY
# # # # for die in range(num_of_dice):
# # # #    for line in dice_art.get(dice[die]):
# # # #        print(line)
# # #
# # # # PRINT HORIZONTALLY
# # # for line in range(5):
# # #     for die in dice:
# # #         print(dice_art.get(die)[line], end="")
# # #     print()
# # #
# # # for die in dice:
# # #     total += die
# # # print(f"total: {total}")
# # #---------------------------------------------------ENCRYPTION TEXT CODE---------------------------------------------------------------------
# # # import random
# # # import string
# # #
# # # chars = " " + string.punctuation + string.digits + string.ascii_letters
# # # chars = list(chars)
# # # key = chars.copy()
# # #
# # # random.shuffle(key)
# # #
# # # #ENCRYPT
# # # plain_text = input("Enter a message to encrypt: ")
# # # cipher_text = ""
# # #
# # # for letter in plain_text:
# # #     index = chars.index(letter)
# # #     cipher_text += key[index]
# # #
# # # print(f"original message : {plain_text}")
# # # print(f"encrypted message: {cipher_text}")
# # #
# # # #DECRYPT
# # # cipher_text = input("Enter a message to encrypt: ")
# # # plain_text = ""
# # #
# # # for letter in cipher_text:
# # #     index = key.index(letter)
# # #     plain_text += chars[index]
# # #
# # # print(f"encrypted message: {cipher_text}")
# # # print(f"original message : {plain_text}")
# # # #---------------------------------------------------BANKING PROGRAM---------------------------------------------------------------------
# # #
# # # def show_balance(balance):
# # #     print("*********************")
# # #     print(f"Your balance is ${balance:.2f}")
# # #     print("*********************")
# # #
# # # def deposit():
# # #     print("*********************")
# # #     amount = float(input("Enter an amount to be deposited: "))
# # #     print("*********************")
# # #     if amount < 0:
# # #         print("*********************")
# # #         print("That's not a valid amount")
# # #         print("*********************")
# # #         return 0
# # #     else:
# # #         return amount
# # #
# # # def withdraw(balance):
# # #     print("*********************")
# # #     amount = float(input("Enter amount to be withdrawn: "))
# # #     print("*********************")
# # #
# # #     if amount > balance:
# # #         print("*********************")
# # #         print("Insufficient funds")
# # #         print("*********************")
# # #         return 0
# # #     elif amount < 0:
# # #         print("*********************")
# # #         print("Amount must be greater than 0")
# # #         print("*********************")
# # #         return 0
# # #     else:
# # #         return amount
# # #
# # # def main():
# # #     balance = 0
# # #     is_running = True
# # #
# # #     while is_running:
# # #         print("*********************")
# # #         print("   Banking Program   ")
# # #         print("*********************")
# # #         print("1.Show Balance")
# # #         print("2.Deposit")
# # #         print("3.Withdraw")
# # #         print("4.Exit")
# # #         print("*********************")
# # #         choice = input("Enter your choice (1-4): ")
# # #
# # #         if choice == '1':
# # #             show_balance(balance)
# # #         elif choice == '2':
# # #             balance += deposit()
# # #         elif choice == '3':
# # #             balance -= withdraw(balance)
# # #         elif choice == '4':
# # #             is_running = False
# # #         else:
# # #             print("*********************")
# # #             print("That is not a valid choice")
# # #             print("*********************")
# # #
# # #     print("*********************")
# # #     print("Thank you! Have a nice day!")
# # #     print("*********************")
# # #
# # # if __name__ == '__main__':
# # #     main()
# # # #---------------------------------------------------SLOTH MACHINE---------------------------------------------------------------------
# #
# # # import random
# # #
# # # def spin_row():
# # #     symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
# # #
# # #     return [random.choice(symbols) for _ in range(3)]
# # #
# # # def print_row(row):
# # #     print("**************")
# # #     print(" | ".join(row))
# # #     print("**************")
# # #
# # # def get_payout(row, bet):
# # #     if row[0] == row[1] == row[2]:
# # #         if row[0] == '🍒':
# # #             return bet * 3
# # #         elif row[0] == '🍉':
# # #             return bet * 4
# # #         elif row[0] == '🍋':
# # #             return bet * 5
# # #         elif row[0] == '🔔':
# # #             return bet * 10
# # #         elif row[0] == '⭐':
# # #             return bet * 20
# # #     return 0
# # #
# # # def main():
# # #     balance = 100
# # #
# # #     print("*************************")
# # #     print("Welcome to Python Slots ")
# # #     print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
# # #     print("*************************")
# # #
# # #     while balance > 0:
# # #         print(f"Current balance: ${balance}")
# # #
# # #         bet = input("Place your bet amount: ")
# # #
# # #         if not bet.isdigit():
# # #             print("Please enter a valid number")
# # #             continue
# # #
# # #         bet = int(bet)
# # #
# # #         if bet > balance:
# # #             print("Insufficient funds")
# # #             continue
# # #
# # #         if bet <= 0:
# # #             print("Bet must be greater than 0")
# # #             continue
# # #
# # #         balance -= bet
# # #
# # #         row = spin_row()
# # #         print("Spinning...\n")
# # #         print_row(row)
# # #
# # #         payout = get_payout(row, bet)
# # #
# # #         if payout > 0:
# # #             print(f"**********You won************** ${payout}")
# # #             print(f"your balane is ${balance}")
# # #         else:
# # #             print("Sorry you lost this round")
# # #
# # #         print(f"your balane is ${balance}")
# # #         play_again = input("Do you want to spin again? (Y/N): ").upper()
# # #
# # #         if play_again != 'Y':
# # #             break
# # #
# # #     print("*******************************************")
# # #     print(f"Game over! Your final balance is ${balance}")
# # #     print("*******************************************")
# # #
# # # if __name__ == '__main__':
# # #     main()
# # # #---------------------------------------------------HANGMAN GAME---------------------------------------------------------------------
# # #
# # # import random
# # #
# # # hangman_art = {0: ("   ",
# # #                                    "   ",
# # #                                    "   "),
# # #                              1: (" o ",
# # #                                    "   ",
# # #                                    "   "),
# # #                              2: (" o ",
# # #                                    " | ",
# # #                                    "   "),
# # #                              3: (" o ",
# # #                                    "/| ",
# # #                                    "   "),
# # #                              4: (" o ",
# # #                                   "/|\\",
# # #                                    "   "),
# # #                               5: (" o ",
# # #                                    "/|\\",
# # #                                    "/  "),
# # #                               6: (" o ",
# # #                                    "/|\\",
# # #                                    "/ \\")}
# # #
# # # words = ("aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant",  "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer", "red-panda", "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra")
# # #
# # # def display_man(wrong_guesses):
# # #     print("**********")
# # #     for line in hangman_art[wrong_guesses]:
# # #         print(line)
# # #     print("**********")
# # #
# # # def display_hint(hint):
# # #     print(" ".join(hint))
# # #
# # # def display_answer(answer):
# # #     print(" ".join(answer))
# # #
# # # def main():
# # #     answer = random.choice(words)
# # #     hint = ["_"] * len(answer)
# # #     wrong_guesses = 0
# # #     guessed_letters = set()
# # #     is_running = True
# # #
# # #     while is_running:
# # #         display_man(wrong_guesses)
# # #         display_hint(hint)
# # #         guess = input("Enter a letter: ").lower()
# # #
# # #         if len(guess) != 1 or not guess.isalpha():
# # #             print("Invalid input")
# # #             continue
# # #
# # #         if guess in guessed_letters:
# # #             print(f"{guess} is already guessed")
# # #             continue
# # #
# # #         guessed_letters.add(guess)
# # #
# # #         if guess in answer:
# # #             for i in range(len(answer)):
# # #                 if answer[i] == guess:
# # #                     hint[i] = guess
# # #         else:
# # #             wrong_guesses += 1
# # #
# # #         if "_" not in hint:
# # #             display_man(wrong_guesses)
# # #             display_answer(answer)
# # #             print("YOU WIN!")
# # #             is_running = False
# # #         elif wrong_guesses >= len(hangman_art) - 1:
# # #             display_man(wrong_guesses)
# # #             display_answer(answer)
# # #             print("YOU LOSE!")
# # #             is_running = False
# # #
# # # if __name__ == "__main__":
# # #     main()
# # #------------------------------------------------------INHERITANCE--------------------------------------------------------------------------------
# # # class Animal:
# # #     def __init__ (self,name,age):
# # #         self.name=name
# # #         self.age=age
# # #
# # #     def eat(self):
# # #         print(f"{self.name} is eating")
# # #     def age(self):
# # #         print(f"{self.name} is {self.age} years old!")
# # #
# # # class Dog(Animal):
# # #     def sound(self):
# # #         print(f"{self.name} is barking")
# # # class Cat(Animal):
# # #     def sound(self):
# # #         print(f"{self.name} is meowing")
# # # class Mice(Animal):
# # #     def sound(self):
# # #          print(f"{self.name} is squeek")
# # #
# # # d=Dog("charlie",10)
# # # c=Cat("mitty",10)
# # # m=Mice("elaka",1)
# # # print(m.name)
# # # d.eat()
# # # d.sound()
# # #--------------------------------------------------PRIME CHECK-------------------------------------------------------------------------
# # # n = int(input("Enter a number: "))
# # # is_prime = True
# # #
# # # if n < 2:
# # #     is_prime = False
# # # else:
# # #     for i in range(2, n):  # Check all numbers from 2 to n-1
# # #         if n % i == 0:
# # #             is_prime = False
# # #             break  # Stop checking if a factor is found
# # #
# # # if is_prime:
# # #     print(f"{n} is a prime number.")
# # # else:
# # #     print(f"{n} is not a prime number.")
# # import datetime
# # time=datetime.datetime.now()
# # time=time.strftime("%H:%M:%S")
# # print((time))
# #--------------------------------------------------------------ALARM----------------------------------------------------------------
# # # Python Alarm Clock
# # import time
# # import datetime
# # import pygame
# #
# #
# # def set_alarm(alarm_time):
# #     print(f"Alarm set for {alarm_time}")
# #     sound_file = "my_music.mp3"
# #     is_running = True
# #
# #     while is_running:
# #         current_time = datetime.datetime.now().strftime("%H:%M:%S")
# #         print(current_time)
# #
# #         if current_time == alarm_time:
# #             print("WAKE UP! 😴")
# #
# #             pygame.mixer.init()
# #             pygame.mixer.music.load(sound_file)
# #             pygame.mixer.music.play()
# #
# #             while pygame.mixer.music.get_busy():
# #                 time.sleep(1)
# #
# #             is_running = False
# #
# #         time.sleep(1)
# #
# #
# # if __name__ == "__main__":
# #     alarm_time = input("Enter the alarm time (HH:MM:SS): ")
# #     set_alarm(alarm_time)
# #--------------------------------------------------------------API FETCH----------------------------------------------------------------
# # import requests
# #
# # base_url = "https://pokeapi.co/api/v2/"
# #
# # def get_pokemon_info(name):
# #     url = f"{base_url}/pokemon/{name}"
# #     response = requests.get(url)
# #
# #     if response.status_code == 200:
# #         pokemon_data = response.json()
# #         return pokemon_data
# #     else:
# #         print(f"Failed to retrieve data {response.status_code}")
# #
# # pokemon_name = input("enter the pokemon name: ")
# # pokemon_info = get_pokemon_info(pokemon_name)
# #
# # if pokemon_info:
# #     print(f"Name: {pokemon_info["name"].capitalize()}")
# #     print(f"Id: {pokemon_info["id"]}")
# #     print(f"Height: {pokemon_info["height"]}")
# #     print(f"Weight: {pokemon_info["weight"]}")
#
# # ------------------------------------------------PyQt5 introduction-----------------------------------------------------------------------
# # import sys
# # from PyQt5.QtWidgets import QApplication, QMainWindow
# # from PyQt5.QtGui import QIcon
# #
# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         self.setWindowTitle("My cool first GUI")
# #         self.setGeometry(700, 300, 500, 500)
# #         #self.setWindowIcon(QIcon("profile_pic.jpg"))
# #
# # def main():
# #     app = QApplication(sys.argv)
# #     window = MainWindow()
# #     window.show()
# #     sys.exit(app.exec_())
# #
# # if __name__ == "__main__":
# #     main()
# # ----------------------------------------------PyQt5 QLabels----------------------------------------------------------------------
# # import sys
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# # from PyQt5.QtGui import QFont
# # from PyQt5.QtCore import Qt
# #
# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         self.setGeometry(700, 300, 500, 500)
# #
# #         label = QLabel("Hello", self)
# #         label.setFont(QFont("Arial", 40))
# #         label.setGeometry(0, 0, 500, 100)
# #         label.setStyleSheet("color: #292929;"
# #                                            "background-color: #6fdcf7;"
# #                                            "font-weight: bold;"
# #                                            "font-style: italic;"
# #                                            "text-decoration: underline;")
# #
# #         # label.setAlignment(Qt.AlignTop)  # VERTICALLY TOP
# #         # label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
# #         # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER
# #
# #         # label.setAlignment(Qt.AlignRight)  # HORIZONTALLY RIGHT
# #         # label.setAlignment(Qt.AlignHCenter)  # HORIZONTALLY CENTER
# #         # label.setAlignment(Qt.AlignLeft)  # HORIZONTALLY LEFT
# #
# #         # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
# #         # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
# #         # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # CENTER & CENTER
# #         # label.setAlignment(Qt.AlignCenter)  # CENTER & CENTER
# #
# # def main():
# #     app = QApplication(sys.argv)
# #     window = MainWindow()
# #     window.show()
# #     sys.exit(app.exec_())
# #
# # if __name__ == "__main__":
# #     main()
# #-------------------------------------------------------------PyQt5 images------------------------------------------------------------
# # import sys
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# # from PyQt5.QtGui import QPixmap
# #
# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         self.setGeometry(700, 300, 500, 500)
# #
# #         label = QLabel(self)
# #         label.setGeometry(0, 0, 500, 500)
# #
# #         pixmap = QPixmap("profile_pic.jpg")
# #         label.setPixmap(pixmap)
# #
# #         label.setScaledContents(True)
# #
# #         label.setGeometry((self.width() - label.width()) // 2,
# #                                           (self.height() - label.height()) // 2,
# #                                            label.width(),
# #                                            label.height())
# #
# # def main():
# #     app = QApplication(sys.argv)
# #     window = MainWindow()
# #     window.show()
# #     sys.exit(app.exec_())
# #
# # if __name__ == "__main__":
# #     main()
#
#
# # # -------------------------------------------Python PyQt5  BATMAN'S Digital Clock-----------------------------------------
# # import sys
# # from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# # from PyQt5.QtCore import QTimer, QTime, Qt
# # from PyQt5.QtGui import QFont, QFontDatabase
# #
# # class DigitalClock(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.time_label = QLabel(self)
# #         self.timer = QTimer(self)
# #         self.initUI()
# #
# #     def initUI(self):
# #         self.setWindowTitle("🦇MAN'S  Digital Clock")
# #         self.setGeometry(600, 400, 300, 100)
# #
# #         vbox = QVBoxLayout()
# #         vbox.addWidget(self.time_label)
# #         self.setLayout(vbox)
# #
# #         self.time_label.setAlignment(Qt.AlignCenter)
# #
# #         self.time_label.setStyleSheet("font-size: 150px;"
# #                                                              "color: hsl(6F6C6C);")
# #         self.setStyleSheet("background-color: darkgrey;")
# #
# #         # Use a custom font
# #         font_id = QFontDatabase.addApplicationFont("Bruce Forever.ttf")
# #         font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
# #         my_font = QFont(font_family, 300)
# #         self.time_label.setFont(my_font)
# #
# #         self.timer.timeout.connect(self.update_time)
# #         self.timer.start(1000)
# #
# #         self.update_time()
# #
# #     def update_time(self):
# #         current_time = QTime.currentTime().toString("hh:mm:ss AP")
# #         self.time_label.setText(current_time)
# #
# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     clock = DigitalClock()
# #     clock.show()
# #     sys.exit(app.exec_())
#
# import sys
# import requests
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
#                                                        QLineEdit, QPushButton, QVBoxLayout)
# from PyQt5.QtCore import Qt
#
# class WeatherApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.city_label = QLabel("Enter city name: ", self)
#         self.city_input = QLineEdit(self)
#         self.get_weather_button = QPushButton("Get Weather", self)
#         self.temperature_label = QLabel(self)
#         self.emoji_label = QLabel(self)
#         self.description_label = QLabel(self)
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("Weather App")
#
#         vbox = QVBoxLayout()
#
#         vbox.addWidget(self.city_label)
#         vbox.addWidget(self.city_input)
#         vbox.addWidget(self.get_weather_button)
#         vbox.addWidget(self.temperature_label)
#         vbox.addWidget(self.emoji_label)
#         vbox.addWidget(self.description_label)
#
#         self.setLayout(vbox)
#
#         self.city_label.setAlignment(Qt.AlignCenter)
#         self.city_input.setAlignment(Qt.AlignCenter)
#         self.temperature_label.setAlignment(Qt.AlignCenter)
#         self.emoji_label.setAlignment(Qt.AlignCenter)
#         self.description_label.setAlignment(Qt.AlignCenter)
#
#         self.city_label.setObjectName("city_label")
#         self.city_input.setObjectName("city_input")
#         self.get_weather_button.setObjectName("get_weather_button")
#         self.temperature_label.setObjectName("temperature_label")
#         self.emoji_label.setObjectName("emoji_label")
#         self.description_label.setObjectName("description_label")
#
#         self.setStyleSheet("""
#             QLabel, QPushButton{
#                 font-family: calibri;
#             }
#             QLabel#city_label{
#                 font-size: 40px;
#                 font-style: italic;
#             }
#             QLineEdit#city_input{
#                 font-size: 40px;
#             }
#             QPushButton#get_weather_button{
#                 font-size: 30px;
#                 font-weight: bold;
#             }
#             QLabel#temperature_label{
#                 font-size: 75px;
#             }
#             QLabel#emoji_label{
#                 font-size: 100px;
#                 font-family: Segoe UI emoji;
#             }
#             QLabel#description_label{
#                 font-size: 50px;
#             }
#         """)
#
#     def get_weather(self):
#         api_key = "77e5c59711b97051531e8b19904e81c4"
#
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     weather_app = WeatherApp()
#     weather_app.show()
#     sys.exit(app.exec_())
#
#
#
#
# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     return fact
#
# def sum_of_digits_factorials(n):
#     sum_fact = 0
#     while n > 0:
#         digit = n % 10  # Extract last digit
#         sum_fact += factorial(digit)  # Add its factorial
#         n //= 10  # Use integer division to remove last digit
#     return sum_fact
#
# def strong_integer(n):
#     if sum_of_digits_factorials(n) == n:
#         print("YES")
#     else:
#         print("NO")
#
# if __name__ == '__main__':
#     n = int(input("ENTER A NUMBER: "))  # Input from user
#     strong_integer(n)  # Check if it's a Strong Number
# Function to Display Game Over Screen
import pygame
import random
import time
import sys

# Initialize Pygame
pygame.init()

# Game Constants
width, height = 600, 600  # Window Size
game_screen = pygame.display.set_mode((width, height + 50))  # Extra 50 pixels for score
pygame.display.set_caption("🐍 Smooth & Realistic Snake Game")

# Colors
BG_COLOR_TOP = (15, 15, 45)
BG_COLOR_BOTTOM = (50, 50, 150)
SNAKE_HEAD_COLOR = (0, 255, 100)
SNAKE_BODY_COLOR = (0, 200, 80)
FOOD_COLOR = (255, 51, 51)
FOOD_GLOW = (255, 102, 102)
BONUS_FOOD_COLOR = (255, 215, 0)
TEXT_COLOR = (255, 255, 255)

# Snake Variables (Reduced Size)
snake_x, snake_y = width // 2, height // 2
change_x, change_y = 15, 0  # Moves in increments of 15
snake_body = [(snake_x, snake_y)]
direction = "RIGHT"

# Food Variables (Reduced Size)
def generate_food():
    while True:
        new_x = random.randrange(0, width, 15)
        new_y = random.randrange(0, height, 15)
        if (new_x, new_y) not in snake_body:
            return new_x, new_y
food_x, food_y = generate_food()

# Bonus Food Settings
bonus_food_x, bonus_food_y = None, None
bonus_food_time = time.time() + 66

# Score
score = 0
game_over = False
font = pygame.font.Font(None, 30)

# Function to Draw Gradient Background
def draw_gradient_background():
    for i in range(height):
        color = (
            BG_COLOR_TOP[0] + (BG_COLOR_BOTTOM[0] - BG_COLOR_TOP[0]) * i // height,
            BG_COLOR_TOP[1] + (BG_COLOR_BOTTOM[1] - BG_COLOR_TOP[1]) * i // height,
            BG_COLOR_TOP[2] + (BG_COLOR_BOTTOM[2] - BG_COLOR_TOP[2]) * i // height,
        )
        pygame.draw.line(game_screen, color, (0, i), (width, i))

# Function to Display Game Over Screen
def display_game_over():
    game_screen.fill((0, 0, 0))  # Clear screen with black
    game_over_text = font.render("GAME OVER", True, TEXT_COLOR)
    final_score_text = font.render(f"Final Score: {score}", True, TEXT_COLOR)
    restart_text = font.render("Press R to Restart", True, TEXT_COLOR)

    # Display Game Over and Score
    game_screen.blit(game_over_text, (width // 2 - 70, height // 2 - 50))
    game_screen.blit(final_score_text, (width // 2 - 80, height // 2))
    game_screen.blit(restart_text, (width // 2 - 100, height // 2 + 50))

    pygame.display.update()

# Function to Display Snake, Food, and Bonus Food
def display_snake_and_food():
    global snake_x, snake_y, food_x, food_y, game_over, score, bonus_food_x, bonus_food_y, bonus_food_time

    # Move Snake
    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height

    # Check Self Collision
    if (snake_x, snake_y) in snake_body[1:]:
        game_over = True
        display_game_over()  # Show Game Over screen
        return

    # Grow Snake
    snake_body.append((snake_x, snake_y))

    # Check Normal Food Collision
    if food_x == snake_x and food_y == snake_y:
        food_x, food_y = generate_food()
        score += 1
    else:
        del snake_body[0]

    # Spawn Bonus Food Every 66 Seconds
    if time.time() >= bonus_food_time and bonus_food_x is None:
        bonus_food_x, bonus_food_y = generate_food()

    # Check Bonus Food Collision
    if bonus_food_x is not None and bonus_food_y is not None:
        if bonus_food_x == snake_x and bonus_food_y == snake_y:
            score += 5
            bonus_food_x, bonus_food_y = None, None
            bonus_food_time = time.time() + 66  # Reset Timer

    # Draw Background
    draw_gradient_background()

    # Draw Normal Food
    pygame.draw.circle(game_screen, FOOD_GLOW, (food_x, food_y), 6)
    pygame.draw.circle(game_screen, FOOD_COLOR, (food_x, food_y), 4)

    # Draw Bonus Food (If Available)
    if bonus_food_x is not None and bonus_food_y is not None:
        pygame.draw.circle(game_screen, BONUS_FOOD_COLOR, (bonus_food_x, bonus_food_y), 10)

    # Draw Snake
    for i, (x, y) in enumerate(snake_body):
        color = SNAKE_HEAD_COLOR if i == len(snake_body) - 1 else SNAKE_BODY_COLOR
        pygame.draw.rect(game_screen, color, (x, y, 15, 15), border_radius=5)  # Rounded snake body

    # Draw Score
    pygame.draw.rect(game_screen, (0, 0, 0), (0, height, width, 50))
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    game_screen.blit(score_text, (width // 2 - 50, height + 10))

    # Update Display
    pygame.display.update()

# Main Game Loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_x, change_y, direction = -15, 0, "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_x, change_y, direction = 15, 0, "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    change_x, change_y, direction = 0, -15, "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_x, change_y, direction = 0, 15, "DOWN"

            if event.key == pygame.K_r:  # Restart game
                snake_x, snake_y = width // 2, height // 2
                change_x, change_y = 15, 0
                score = 0
                snake_body = [(snake_x, snake_y)]
                bonus_food_x, bonus_food_y = None, None
                bonus_food_time = time.time() + 66
                game_over = False

    if not game_over:
        display_snake_and_food()
        clock.tick(10)  # Smooth game speed