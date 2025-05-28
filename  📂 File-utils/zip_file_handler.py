# Extração de arquivos de um ZIP

import zipfile

with zipfile.ZipFile("arquivo.zip", "r") as zip_ref:
    zip_ref.extractall("destino/")
