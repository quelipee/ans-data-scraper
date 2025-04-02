import os
import zipfile


class Compactador:
    def __init__(self, list_anexo: list, zip_name: str) -> None:
        self.list_anexo = list_anexo
        self.zip_name = zip_name

    def extract_for_zip(self):
        if os.path.exists('./code/web_scraping/' + self.zip_name):
            print('There is already a zip file')
        else:
            with zipfile.ZipFile('./code/web_scraping/' + self.zip_name, 'w') as zip:
                for link in self.list_anexo:
                    zip.write('./code/web_scraping/' + link, arcname=link)
                    os.remove('./code/web_scraping/' + link)
