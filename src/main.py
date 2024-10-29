import dotenv
import os
from speaak_with_gpt import SpeakWithGPT
from web_scraper import WebScraper

#todo this should be passed from client side
GPT_analyzer_as = ("You are DevOps engineer with knowledge of python and "
                   "looking for job title return only answer 1 or 0 if it is compatible title for you knowledge")

dotenv.load_dotenv("../.env")

OPENAI_API_KEY : str = os.getenv("OPENAI_API_KEY")
SITES_URL : list[str] = [os.getenv("SITES_URL")] #for testing purposes after development it should take list of urls

web_scraper = WebScraper(SITES_URL)
applications = web_scraper.turn_into_list()


gpt = SpeakWithGPT(system_role=GPT_analyzer_as)
#todo this code is checking titles of applications and using chatgpt api evaluates whether it is useful or not
#move this to class in future when you create logic class
for application in applications:
    application["useful"] = gpt.prompt(application["title"]).choices[0].message.content
