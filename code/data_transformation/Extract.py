import os
import zipfile
import pandas as pd

import pdfplumber

from code.interface.Compact import Compact


class Extract(Compact):
    def __init__(self, list_anexo: list, zip_name: str):

        super().__init__(list_anexo, zip_name)

    def extract_data(self) -> None:
        data_table = []
        procecimentos = 'procecimentos.csv'
        if "Anexo I.pdf" in self.list_anexo:
            index = self.list_anexo.index('Anexo I.pdf')
            if not zipfile.is_zipfile('./code/web_scraping/' + self.zip_name):
                raise Exception('Zip file not found')

            with zipfile.ZipFile('./code/web_scraping/' + self.zip_name, 'r') as z:
                z.extract(self.list_anexo[index], './code/data_transformation/')
            with pdfplumber.open('./code/data_transformation/' + self.list_anexo[index]) as pdf:
                for page in pdf.pages:
                    texto = page.extract_table()
                    if texto:
                        data_table.extend(texto)  # Adiciona as linhas diretamente

                df = pd.DataFrame(data_table[1:], columns=data_table[0])  # Primeira linha como cabeçalho
                df.replace({"OD": "Odontológica", "AMB": "Ambulatorial"},
                           inplace=True)  # substituindo nome dos valores dessa coluna
                df.to_csv(procecimentos, index=False, encoding='utf-8-sig')
                self.extract_for_zip(procecimentos)

    def extract_for_zip(self, procedimentos_csv):
        test_zip = os.getenv('ZIP_TEST_NAME')
        if os.path.exists(test_zip):
            print('There is already a zip file')
            return test_zip
        else:
            with zipfile.ZipFile(test_zip, 'w') as zip:
                zip.write(procedimentos_csv, arcname=procedimentos_csv)
                os.remove(procedimentos_csv)
            return self.zip_name
