import requests
import os


def download_image(url, images_dir, filename):
    image_link = requests.get(url)
    with open(os.path.join(images_dir, filename), 'wb') as file:  
        file.write(image_link.content)


def fetch_hubble_collection(hubble_collection):
    url = 'http://hubblesite.org/api/v3/images/{}'.format(hubble_collection)
    collection_ids = []
    for elem in requests.get(url).json():
        collection_ids.append(elem['id'])
    return collection_ids
    
    
def fetch_hubble_image(images_dir, image_id):
    url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    image_link = requests.get(url).json()['image_files'][-1]['file_url']
    extension = image_link.split('.')[-1]
    download_image(image_link, images_dir, '{}.{}'.format(image_id, extension))


if __name__ == '__main__':
    images_dir = 'images'
    hubble_collection = 'spacecraft'
    if not os.path.exists(images_dir):
        os.mkdir(images_dir)
        
    for id in fetch_hubble_collection(hubble_collection):
        fetch_hubble_image(images_dir, id)
