# This script is a simple agreement bot that asks the user for their favorite animal
# and responds with a message indicating that the bot's favorite animal is the same.
def main():

    animal = input("\033[1;3m What's your favorite animal? \033[0m")
    print(f"My favorite animal is also {animal}!")

if __name__ == '__main__':
    main()