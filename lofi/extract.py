import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
from .youtube import youtube

'''
With help from KISHAN MALADKAR's Using Natural Language Processing To Check Word Frequency In 
‘The Adventure of Sherlock Holmes’
'''

# nltk.download('stopwords')

def article_request(link, freq, rand):
    request = requests.get(link)
    html = request.text

    soup = BeautifulSoup(html, "html.parser")
    # print(soup.title.string)
    # print(soup.find_all('a'))

    text = soup.get_text()
    return text_request(text, freq, rand)


def text_request(text, freq, rand):
    tokens = re.findall('\w+', text)
    # print(tokens[:10])

    # transform all tokens into lowercase so that they all have the same spelling
    tokens = [token.lower() for token in tokens]
    # print(tokens[:10])

    stop_words = ['the', 'and', 'of', 'to', 'in', 'a', 's']
    # get the stop words in english
    # stop_words = nltk.corpus.stopwords.words('english')
    # print(stop_words)

    tokens = [token for token in tokens if token not in stop_words]

    counts = Counter(tokens)
    # print(counts.most_common(freq))

    # get the x most frequent words
    word_dict = counts.most_common(freq)
    top_words = []
    for key, item in word_dict:
        top_words.append(key)
    search_query = " ".join(top_words)
    return youtube(search_query, freq, rand)
