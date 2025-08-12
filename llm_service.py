import os
import asyncio
from typing import Dict, Any

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def _call_openai_chat(messages):
    # Delayed import to avoid errors when key missing.
    import openai
    openai.api_key = OPENAI_API_KEY
    resp = openai.ChatCompletion.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4"),
        messages=messages,
        temperature=0.2,
        max_tokens=500
    )
    return resp["choices"][0]["message"]["content"]

async def ask_llm_endpoint(query: str, context: Dict[str, Any]):
    """
    Simple wrapper that composes a system prompt + context + user query,
    then calls the LLM. If OPENAI_API_KEY is not set, returns a deterministic stub.
    """
    if not query:
        return {"error": "empty query"}

    system_prompt = (
        "You are ThalCare AI — a helpful assistant specialized in thalassemia management. "
        "Always provide safe, evidence-based, non-diagnostic guidance, and recommend contacting a clinician for clinical decisions."
    )

    # Optionally inject patient summary into prompt for personalization
    patient_summary = ""
    if context:
        parts = []
        for k, v in context.items():
            parts.append(f"{k}: {v}")
        patient_summary = "Patient summary:\n" + "\n".join(parts)

    messages = [
        {"role": "system", "content": system_prompt},
    ]
    if patient_summary:
        messages.append({"role": "system", "content": patient_summary})
    messages.append({"role": "user", "content": query})

    if OPENAI_API_KEY:
        try:
            content = await _call_openai_chat(messages)
            return {"answer": content}
        except Exception as e:
            return {"error": f"LLM error: {str(e)}"}
    else:
        # Stubbed deterministic reply when OpenAI key not present
        stub = (
            "This is a demo response from ThalCare AI (OpenAI key not configured). "
            "For example purposes, here is suggested educational content. "
            "Please consult a doctor for any medical decision."
        )
        return {"answer": stub}

