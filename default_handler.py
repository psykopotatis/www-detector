from bs4 import BeautifulSoup


def handle(r):
    print("default_handler")
    return r.text
