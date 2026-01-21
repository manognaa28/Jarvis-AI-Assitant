from pinecone_client import pc, index

with open("../data/docs.txt", "r", encoding="utf-8") as f:
    docs = [line.strip() for line in f if line.strip()]

# REQUIRED: input_type="passage" for documents
embeddings = pc.inference.embed(
    model="llama-text-embed-v2",
    inputs=docs,
    parameters={"input_type": "passage"}
)

vectors = []
for i, emb in enumerate(embeddings):
    vectors.append({
        "id": f"doc-{i}",
        "values": emb["values"],
        "metadata": {"text": docs[i]}
    })

index.upsert(vectors)
print("Documents successfully ingested into Pinecone")
