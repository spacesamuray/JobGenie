import dotenv
import os
import requests

from speaak_with_gpt import SpeakWithGPT
from web_scraper import WebScraper
from selector import Selector

#todo this should be passed from client side
gpt_title_analyzer_role = ("You are DevOps engineer with knowledge of linux,networking,infrastructure,pipelines and python"
                   "looking for job title return only answer 1 or 0 if it is compatible title for you knowledge")
gpt_application_analyzer_role = ("You are senior DevOps engineer with knowledge of linux,networking,infrastructure,cloud"
                               ",pipelines and python looking for job return only email or 0 depending if your suitable or not follwing application")

dotenv.load_dotenv("../.env")

OPENAI_API_KEY : str = os.getenv("OPENAI_API_KEY")
SITES_URL : list[str] = [os.getenv("SITES_URL")] #for testing purposes after development it should take list of urls

web_scraper = WebScraper(SITES_URL)
applications = web_scraper.turn_titles_into_list()

#Creating GPT's with their respective roles
gpt_title_analyzer = SpeakWithGPT(system_role=gpt_title_analyzer_role) #For analyzing titles
gpt_application_analyzer = SpeakWithGPT(system_role=gpt_application_analyzer_role) #For analyzing applications itself

useful_titles = Selector.select_titles(gpt_model=gpt_title_analyzer, titles=applications)

applications_urls = [title["url"] for title in useful_titles]
applications_bs4_list = web_scraper.scrap_web(applications_urls)
web_scraper.APPLICATIONS_HTML = applications_bs4_list #todo refactor this code so that it could be understandable
applications = web_scraper.turn_applications_into_list()
print(applications)
# useful_applications = Selector.select_application(gpt_model=gpt_application_analyzer)
# print(useful_titles)



