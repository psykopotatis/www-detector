from bs4 import BeautifulSoup
import requests
import hashlib
import pickler


url = "URL-HERE"
pickle_file = "hash.pickle"
print("[GET] %s" % url)
r = requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.text, 'html.parser')
pipeline = soup.find(id="pipeline")

hash = hashlib.md5(pipeline.encode('utf-8')).hexdigest()
print(hash)
previous_hash = pickler.load(pickle_file, "asdf")
print(previous_hash)

if previous_hash == hash:
    print("Same: %s" % url)
else:
    print("Change detected: %s" % url)
    pickler.dump(pickle_file, hash)
