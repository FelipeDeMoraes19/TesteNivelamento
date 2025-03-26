from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df_operadoras = pd.read_csv('Relatorio_cadop.csv', delimiter=';', encoding='latin1')
df_operadoras.replace({np.nan: '', np.inf: '', -np.inf: ''}, inplace=True)

@app.get("/buscar/")
async def buscar_operadoras(texto: str = Query(..., min_length=3)):
    resultado = df_operadoras[
        df_operadoras.apply(lambda row: row.astype(str).str.contains(texto, case=False).any(), axis=1)
    ]
    resultado = resultado.fillna('').astype(str)
    return resultado.head(10).to_dict(orient='records')
