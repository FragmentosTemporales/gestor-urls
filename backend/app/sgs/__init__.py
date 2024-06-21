import os
import json
import csv


class SGS:
    def __init__(self, ruta):

        self.ruta = ruta
        url = f"{self.ruta}/app/data/data.json"
        new_url = f"{self.ruta}/app/downloads/data.json"
        csv_url = f"{self.ruta}/app/downloads/test.csv"

        data = self.load_data(url)

        self.save_data(data=data, url=new_url)
        self.create_empty_csv(csv_url)

    def load_data(self, url):
        try:
            with open(url, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {url}")
        except IsADirectoryError:
            raise IsADirectoryError("La ruta especificada es un directorio")
        except json.JSONDecodeError:
            raise ValueError("El archivo no contiene un JSON válido")
        except Exception as e:
            raise Exception("Error inesperado") from e

    def save_data(self, data, url):
        try:
            os.makedirs(os.path.dirname(url), exist_ok=True)
            with open(url, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Data guardada en: {url}")
        except Exception as e:
            raise Exception("Error inesperado") from e

    def create_empty_csv(self, url):
        try:
            with open(url, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([])
            print("Archivo CSV vacío guardado")
        except Exception as e:
            raise Exception("Error inesperado") from e
