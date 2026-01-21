from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from pinecone_client import pc, index

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    html = Path("../frontend/index.html").read_text(encoding="utf-8")
    return html

@app.post("/chat")
def chat(query: str):
    query_embedding = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=[query],
        parameters={"input_type": "query"}
    )[0]["values"]

    result = index.query(
        vector=query_embedding,
        top_k=2,
        include_metadata=True
    )

    answer = result["matches"][0]["metadata"]["text"]
    return {"response": answer}
