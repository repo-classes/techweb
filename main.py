from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from validator import validate_cpf

app = FastAPI(
    title="Validador de CPF",
    description="API para validar CPF brasileiro",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Validador de CPF rodando! Use /api/validar?cpf=..."}
    

@app.get("/api/validar")
def validar_cpf_endpoint(
    cpf: str = Query(..., description="CPF com ou sem máscara (ex: 12345678901 ou 123.456.789-01)")
):
    if not cpf:
        raise HTTPException(status_code=400, detail="Parâmetro 'cpf' é obrigatório")

    valido = validate_cpf(cpf)

    return JSONResponse(
        content={
            "cpf": cpf,
            "valido": valido,
            "mensagem": "CPF válido" if valido else "CPF inválido"
        },
        status_code=200
    )

# Documentação automática em /docs (Swagger) e /redoc