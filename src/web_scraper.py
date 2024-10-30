from bs4 import BeautifulSoup
import requests

class WebScraper:

    DOMAIN_ROOTS : list[str]
    TITLES_URLS : list[str]
    TITLES_HTML : list[BeautifulSoup]


    def __init__(self, urls):
        self.DOMAIN_ROOTS = [f"{url[:8]}{url[8::].split('/')[0]}" for url in urls] # This is constructing url root for future usage
        self.TITLES_URLS = urls
        self.TITLES_HTML = self.scrap_web(self.TITLES_URLS)#[BeautifulSoup(requests.get(url).text, 'html.parser') for url in self.URLS]

    #for testing, it is built for jobs.ge
    #this part should be taken cared by chatgpt which evaluates and writes unique selector for any sites we pass in
    def fetch_applications_(self) -> list:
        """
        This method takes each table row from whole html and turns it into a list[Bs4<object>]
        :return: list of table data elements
        """
        table_rows = self.TITLES_HTML[0].select(".regularEntries tr")
        return [row.select("td")[1] for row in table_rows if len(row.select("td")) > 0]

    def turn_titles_into_list(self) -> list[dict[str, str]]:
        """
        This method is responsible for turning  BeautifulSoups objects into a list of dictionaries.
        :return: list[dict[str, str]]
        """
        application_list : list[dict[str,str]] = []
        for table_data in self.fetch_applications_():
            link = table_data.find("a")
            application_list.append(
                {
                    "title": link.string,
                    "url": link.get("href"),
                }
            )
        return application_list

    #todo write this methods logic
    def turn_pages_into_list(self) -> list[dict[str, str]]:
        """
        This method is responsible for turning BeautifulSoups objects into a list of dictionaries.
        :return: list[dict[str, str]]
        """
        # pages_list : list[dict[str,str]] = []
        pass


    @staticmethod
    def scrap_web(urls : list[str]) -> list[BeautifulSoup]:
        """
        This method is responsible for scraping web pages. and then turns it into a list of BeautifulSoups object.
        :param urls:
        :return list[BeautifulSoup]:
        """
        return [BeautifulSoup(requests.get(url).text,"html.parser") for url in urls]
