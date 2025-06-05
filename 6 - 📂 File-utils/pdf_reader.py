# Leitura de PDF com PyMuPDF

import fitz  # PyMuPDF

doc = fitz.open("documento.pdf")
for page in doc:
    print(page.get_text())
