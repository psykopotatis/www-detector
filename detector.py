import requests
import hashlib
import pickler
from targets import targets
from slugify import slugify
from mailer import Mailer


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
        m = Mailer()
        m.send_email("Change detected!", "headers", url)
        pickler.dump(pickle_file, hash)
