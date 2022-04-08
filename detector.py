import requests
import hashlib
import pickler
from targets import targets
from slugify import slugify


for target in targets:
    url, handler = target

    pickle_file = slugify(url) + ".pickle"
    print("[GET] %s" % url)
    r = requests.get(url)

    result = handler.handle(r)

    hash = hashlib.md5(result.encode('utf-8')).hexdigest()
    previous_hash = pickler.load(pickle_file, "asdf")

    if previous_hash == hash:
        print("Same!")
    else:
        print("Change detected!")
        pickler.dump(pickle_file, hash)
