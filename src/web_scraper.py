from bs4 import BeautifulSoup
import requests

class WebScraper:

    URLS : list[str]
    HTML : list[BeautifulSoup]

    def __init__(self, urls):
        self.URLS = urls
        self.HTML = [BeautifulSoup(requests.get(url).text, 'html.parser') for url in self.URLS]


    # @staticmethod
    # def get_html(url) -> BeautifulSoup:
    #     """
    #     Returns a BeautifulSoup object from a given URL.
    #     :param url: desired url to return html
    #     :return: BeautifulSoup object which contains html of desired url
    #     """
    #     response = requests.get(url)
    #     return BeautifulSoup(response.text, 'html.parser')
