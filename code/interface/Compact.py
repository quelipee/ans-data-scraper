from abc import ABC


class Compact(ABC):
    def __init__(self, list_anexo: list, zip_name: str) -> None:
        self.list_anexo = list_anexo
        self.zip_name = zip_name

    @staticmethod
    def extract_for_zip(self):
        pass