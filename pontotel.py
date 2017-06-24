import hug
import requests


@hug.local()
def get_occurrences(url: hug.types.text, key_word: hug.types.text):
    """
    Returns JSON containing number of occurrences of "key_word" in website
    given by "url"
    """
    content = requests.get(url).content
    html_text = content.decode('utf-8')
    from bs4 import BeautifulSoup
    #print (BeautifulSoup(html_text, "lxml").get_text())
    text = BeautifulSoup(html_text, "lxml").get_text().split()
    counter = 0
    for word in text:
        if word == key_word:
            counter += 1
    string = '{{"{0}": "{1}"}}'.format("Occurrences", counter)
    return (string)
