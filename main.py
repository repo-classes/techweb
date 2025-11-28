# main.py
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from documentos import validar_cpf, validar_cnpj

app = FastAPI(
    title="Validador de CPF e CNPJ",
    description="API para validar CPF e CNPJ brasileiros",
    version="1.0.1"
)

@app.get("/")
def root():
    return {
        "message": "Validador de CPF/CNPJ ativo!",
        "endpoints": {
            "CPF": "/api/validar?cpf=12345678909",
            "CNPJ": "/api/validar?cnpj=11222333000199"
        }
    }

def _resposta_padrao(documento: str, valido: bool, tipo: str):
    return {
        tipo.lower(): documento,
        "valido": valido,
        "mensagem": f"{tipo} válido" if valido else f"{tipo} inválido"
    }

@app.get("/api/validar")
def validar_documento(
    cpf: str = Query(None, description="CPF com ou sem máscara"),
    cnpj: str = Query(None, description="CNPJ com ou sem máscara")
):
    if cpf and cnpj:
        raise HTTPException(
            status_code=400,
            detail="Envie apenas um parâmetro: 'cpf' ou 'cnpj', não ambos."
        )
    
    if not cpf and not cnpj:
        raise HTTPException(
            status_code=400,
            detail="Parâmetro obrigatório: 'cpf' ou 'cnpj'"
        )

    if cpf:
        valido = validar_cpf(cpf)
        return JSONResponse(content=_resposta_padrao(cpf, valido, "CPF"), status_code=200)
    
    if cnpj:
        valido = validar_cnpj(cnpj)
        return JSONResponse(content=_resposta_padrao(cnpj, valido, "CNPJ"), status_code=200)