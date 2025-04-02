from dotenv import load_dotenv

from code.web_scraping.Compactador import Compactador
from code.web_scraping.Scraper import Scraper
import os

load_dotenv()

scraper = Scraper(os.getenv('URL_ANEXOS'))
return_scraper = scraper.run()
compactor = Compactador(return_scraper, 'anexo.zip')
compactor.extract_for_zip()
