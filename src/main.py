import dotenv
import os

dotenv.load_dotenv("../.env")

API_KEY : str = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")
print(API_KEY)
