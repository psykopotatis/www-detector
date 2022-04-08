from bs4 import BeautifulSoup


def handle(r):
    print("pipeline_handler")
    soup = BeautifulSoup(r.text, 'html.parser')
    pipeline = soup.find(id="pipeline")
    return pipeline
