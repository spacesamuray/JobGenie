import dotenv
import os
from speaak_with_gpt import SpeakWithGPT
from web_scraper import WebScraper
from selector import Selector

#todo this should be passed from client side
GPT_analyzer_as = ("You are Data analytics with knowledge of python and Sql"
                   "looking for job title return only answer 1 or 0 if it is compatible title for you knowledge")

dotenv.load_dotenv("../.env")

OPENAI_API_KEY : str = os.getenv("OPENAI_API_KEY")
SITES_URL : list[str] = [os.getenv("SITES_URL")] #for testing purposes after development it should take list of urls

web_scraper = WebScraper(SITES_URL)
applications = web_scraper.turn_titles_into_list()

gpt = SpeakWithGPT(system_role=GPT_analyzer_as)
useful_applications = Selector.select_titles(gpt_model=gpt,applications=applications)



