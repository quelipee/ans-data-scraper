import os
import zipfile

from code.interface.Compact import Compact


class Compactador(Compact):
    def __init__(self, list_anexo: list, zip_name: str):
        super().__init__(list_anexo, zip_name)

    def extract_for_zip(self):
        if os.path.exists('./code/web_scraping/' + self.zip_name):
            print('There is already a zip file')
            return  self.zip_name
        else:
            with zipfile.ZipFile('./code/web_scraping/' + self.zip_name, 'w') as zip:
                for link in self.list_anexo:
                    zip.write('./code/web_scraping/' + link, arcname=link)
                    os.remove('./code/web_scraping/' + link)
            return self.zip_name
