'''
python3 utils/simple_download.py
'''
from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ['dragon fruit','dragon fruit plan']


for kw in keywords:
    print('Searching',kw)
    response().download(kw, 50)