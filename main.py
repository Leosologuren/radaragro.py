from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Radar Agro Econômico e Geopolítico")

class RadarResponse(BaseModel):
    slide_1_capa: str
    slide_2_agricultura: str
    slide_3_macro: str
    slide_4_geopolitica: str
    slide_5_conclusao: str
    slide_6_chamada: Optional[str] = None
    slide_7_encerramento: Optional[str] = None

@app.get("/")
def home():
    return {"mensagem": "API do Radar Agro está rodando."}

@app.post("/gerar_radar", response_model=RadarResponse)
def gerar_radar():
    return RadarResponse(
        slide_1_capa="Radar Agro Econômico e Geopolítico - 12 de Julho",
        slide_2_agricultura="📈 Soja fecha em alta com demanda chinesa e clima nos EUA.",
        slide_3_macro="📊 Copom mantém juros, mas sinaliza corte em setembro.",
        slide_4_geopolitica="🌍 Tensão no Mar Negro eleva preços dos grãos.",
        slide_5_conclusao="📌 Clima, juros e exportações em foco: produtores devem redobrar atenção nos próximos 15 dias.",
        slide_6_chamada="🔔 Siga o Radar Agro para atualizações diárias!",
        slide_7_encerramento="Produzido com inteligência artificial 🌱"
    )
