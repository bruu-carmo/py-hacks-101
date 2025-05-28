# Exemplo de uso básico de pandas

import pandas as pd

df = pd.DataFrame({
    "Nome": ["Ana", "Bia", "Carlos"],
    "Idade": [22, 27, 31]
})

print("Quantidade de linhas:", len(df))
