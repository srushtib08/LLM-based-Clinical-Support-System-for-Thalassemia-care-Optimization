from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes_patient import router as patient_router
from backend.llm_service import ask_llm_endpoint

app = FastAPI(title="ThalCare AI - Backend")

# CORS for Streamlit frontend running locally
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patient_router, prefix="/api/patients", tags=["patients"])

@app.post("/api/ask-llm")
async def ask_llm(payload: dict):
    """
    Expects {"query": "<user question>", "context": {...optional patient context...}}
    """
    query = payload.get("query", "")
    context = payload.get("context", {})
    return await ask_llm_endpoint(query, context)


