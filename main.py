from dotenv import load_dotenv

from code.web_scraping.Compactador import Compactador
from code.web_scraping.Scraper import Scraper
import os

load_dotenv()
# print(os.getenv('URL_ANEXOS'))

scraper = Scraper(os.getenv('URL_ANEXOS'))
return_scraper = scraper.run()
compactador = Compactador('anexos.zip')
compactador.extract_for_zip()
