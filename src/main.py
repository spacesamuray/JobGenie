import dotenv
import os
from speaak_with_gpt import SpeakWithGPT
from web_scraper import WebScraper

dotenv.load_dotenv("../.env")

OPENAI_API_KEY : str = os.getenv("OPENAI_API_KEY")
SITES_URL : list[str] = [os.getenv("SITES_URL")] #for testing purposes after development it should take list of urls

web_scraper = WebScraper(SITES_URL)
print(web_scraper.DOMAIN_ROOTS)


# gpt = SpeakWithGPT()
# print(gpt.prompt("How much of human body is water?").choices[0].message.content)
