import os
from instabot import Bot


bot = Bot()
bot.login()


def upload_image(filepath):
    for file in os.listdir(filepath):
        if os.path.isfile(os.path.join(filepath, file)):
            bot.upload_photo(os.path.join(filepath, file))


if __name__ == '__main__':
    filepath = 'images'
    if os.path.exists(filepath) and os.listdir(filepath):
        upload_image(filepath)
    else:
        print("Directory doesn't exist or empty")
