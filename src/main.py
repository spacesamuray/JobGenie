import dotenv
import os
from speaak_with_gpt import SpeakWithGPT

dotenv.load_dotenv("../.env")

OPENAI_API_KEY : str = os.getenv("OPENAI_API_KEY")

gpt = SpeakWithGPT()
print(gpt.prompt("How much of human body is water?").choices[0].message.content)
