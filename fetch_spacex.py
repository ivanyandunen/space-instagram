import requests
import os


def save_image(url, filepath, filename):
    request = requests.get(url)
    with open(os.path.join(filepath, filename), 'wb') as file:  
        file.write(request.content)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches/latest"
    list_of_links = requests.get(url).json()['links']['flickr_images']
    for counter, link in enumerate(list_of_links, 1):
        save_image(link, filepath, 'spacex{}.jpg'.format(counter))


if __name__ == '__main__':
    filepath = 'images'
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    fetch_spacex_last_launch()