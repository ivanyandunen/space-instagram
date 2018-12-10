import os
from instabot import Bot


bot = Bot()
bot.login()


def upload_images(images_dir):
    for file in os.listdir(images_dir):
        if os.path.isfile(os.path.join(images_dir, file)):
            bot.upload_photo(os.path.join(images_dir, file))


if __name__ == '__main__':
    images_dir = 'images'
    if os.path.exists(images_dir) and os.listdir(images_dir):
        upload_image(images_dir)
    else:
        print("Directory doesn't exist or empty")
