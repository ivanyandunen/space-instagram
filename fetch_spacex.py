import requests
import os


def download_image(url, images_dir, filename):
    image_link = requests.get(url)
    with open(os.path.join(images_dir, filename), 'wb') as file:  
        file.write(image_link.content)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches/latest"
    list_of_links = requests.get(url).json()['links']['flickr_images']
    for counter, link in enumerate(list_of_links, 1):
        download_image(link, images_dir, 'spacex{}.jpg'.format(counter))


if __name__ == '__main__':
    images_dir = 'images'
    if not os.path.exists(images_dir):
        os.mkdir(images_dir)
    fetch_spacex_last_launch()
