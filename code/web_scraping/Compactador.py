import os
import zipfile


class Compactador:
    def __init__(self, name_anexo: str):
        self.name_anexo = name_anexo

    def extract_for_zip(self):
        if os.path.exists('./code/web_scraping/' + self.name_anexo):
            print('Compactador existe')
        else:
            with zipfile.ZipFile('./code/web_scraping/anexos.zip', 'w') as zip_ref:
                zip_ref.write('./code/web_scraping/Anexo I.pdf', arcname='Anexo I.pdf')
                zip_ref.write('./code/web_scraping/Anexo II.pdf', arcname='Anexo II.pdf')
