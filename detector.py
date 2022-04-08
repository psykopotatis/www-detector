from bs4 import BeautifulSoup
import requests
import hashlib
import pickler
from urls import urls
from slugify import slugify


for url in urls:
    pickle_file = slugify(url) + ".pickle"
    print("[GET] %s" % url)
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    pipeline = soup.find(id="pipeline")

    hash = hashlib.md5(pipeline.encode('utf-8')).hexdigest()
    print(hash)
    previous_hash = pickler.load(pickle_file, "asdf")
    print(previous_hash)

    if previous_hash == hash:
        print("Same!")
    else:
        print("Change detected!")
        pickler.dump(pickle_file, hash)
