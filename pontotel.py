import hug
import requests

@hug.local()
def get_occurrences(url: hug.types.text, key_word: hug.types.text):
    """
    Returns JSON containing number of occurrences of "key_word" in website
    given by "url"
    """
    # get and decode web content
    content = requests.get(url).content
    html_text = content.decode('utf-8')

    # remove Javascript, CSS and HTML
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_text, "lxml")
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    text = soup.get_text()

    # print(text) #for testing
    # split text into iterable list of words
    text = text.split()

    # count keyword occurrences
    counter = 0
    for word in text:
        if word == key_word:
            counter += 1

    return ('{{"{0}": "{1}"}}'.format("Occurrences", counter))
