from bs4 import BeautifulSoup


def handle(r):
    print("section_handler")
    soup = BeautifulSoup(r.text, 'html.parser')
    # section = soup.find(id="section-one")
    sections = soup.findAll("section", id=lambda x: x and x.startswith('section-'))
    result = ""
    for section in sections:
        result = result + section.prettify()
    return result
