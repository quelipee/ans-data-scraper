from dotenv import load_dotenv

from code.data_transformation.Extract import Extract
from code.database.ANSDataProcessor import ANSDataProcessor
from code.database.QueryTopOperators import QueryTopOperators
from code.web_scraping.Compactador import Compactador
from code.web_scraping.Scraper import Scraper
import os

# load_dotenv()
#
# scraper = Scraper(os.getenv('URL_ANEXOS'))
# return_scraper = scraper.run()
# compactor = Compactador(return_scraper, os.getenv('ZIP_NAME'))
# compact_name = compactor.extract_for_zip()
#
# # Extract arquive anexoI.pdf
#
# extract = Extract(return_scraper,compact_name)
# extract.extract_data()

dbconfig = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : 'root',
    'dbname' : 'ans_operadoras',
}
# ansData = ANSDataProcessor(**dbconfig)
# ansData.create_table()
query_last_quarter = QueryTopOperators(**dbconfig)
# query_last_quarter.get_top_10_expenses_last_quarter()
query_last_quarter.get_top_10_expenses_last_year()