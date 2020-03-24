# Image-Captioning-API

Implemented a show and tell model trained on Flickr 8K dataset to generate image captions

**Steps to download this repo, run in your local server and work on it accordingly:**

**Step 1.** Download or clone this repo.

**Step 2.** Create a glove Folder inside the repo and download this file from the link and paste it inside the glove folder https://drive.google.com/file/d/1Ob9TM2C9qooDFjix8PUW6USpygJSYXh3/view?usp=sharing (note-it is very big so couldn't upload it in the github)

**Step 3.** Get the requirments by typing in the command. `pip install -r requirements.txt`

**Step 4.** RUN `python server.py`

**Step 5.** Get the caption by running the following command:

`curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=<image filepath>" http://127.0.0.1:8000/getCaption`


**Jupyter notebook can also be used for interactive generation captions.**
