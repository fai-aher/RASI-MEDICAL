from fastapi import FastAPI

app = FastAPI()

# Endpoint to check health
@app.get("/health")
def health():
    return {"status": "ok"}

