# Space Instagram

Script `fetch_spacex.py` allows to download images from the latest Space-X launch.

Script `fetch_hubble.py` allows to download images from [Hubblesite](hubblesite.org) image gallery by category.

Script `upload_to instagram.py` allows to upload this images to instagram account.

## How to install

Python 3 has to be installed. You might have to run python3 instead of python depending on system if there is a conflict with Python2. Then use pip (or pip3) to install dependencies:

```commandline
pip install -r requirements.txt
```

Run `python %scriptname.py%`. Downloaded images are saved to `images` subdirectory where scripts run.
To upload images you will need to enter instagram login and password. They are saved to `secret.txt` file in script directory(as `email:=password`. If you have several accounts, they are saved on the new line each).

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).