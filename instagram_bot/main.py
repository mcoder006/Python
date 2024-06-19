from instabot import Bot
from dotenv import load_dotenv
import os

load_dotenv()

def bot():
    username = os.getenv("username")
    password = os.getenv("password")
    # email = os.getenv("email")
    bot = Bot()
    bot.login(username=username, password=password)
    bot.follow('ghimiresushank')
    print("Completed!")


def main():
    bot()

if __name__ == "__main__":
    main()