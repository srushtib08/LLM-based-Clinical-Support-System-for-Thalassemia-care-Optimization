from fastapi import FastAPI, HTTPException
from backend.llm_service import get_llm_response
from backend.patient_data import QueryRequest

app = FastAPI()

@app.post("/ask")
def ask_llm(query: QueryRequest):
    try:
        result = get_llm_response(query.patient_query)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
