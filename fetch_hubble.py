import requests
import os


def save_image(url, filepath, filename):
    request = requests.get(url)
    with open(os.path.join(filepath, filename), 'wb') as file:  
        file.write(request.content)


def fetch_hubble_collection(hubble_collection):
    url = 'http://hubblesite.org/api/v3/images/{}'.format(hubble_collection)
    collection_ids = []
    for elem in requests.get(url).json():
        collection_ids.append(elem['id'])
    return collection_ids
    
    
def fetch_hubble_image(filepath, image_id):
    url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)
    image_link = requests.get(url).json()['image_files'][-1]['file_url']
    extension = image_link.split('.')[-1]
    save_image(image_link, filepath, '{}.{}'.format(image_id, extension))


if __name__ == '__main__':
    filepath = 'images'
    hubble_collection = 'spacecraft'
    if not os.path.exists(filepath):
        os.mkdir(filepath)
        
    for id in fetch_hubble_collection(hubble_collection):
        fetch_hubble_image(filepath, id)