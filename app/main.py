from fastapi import FastAPI

app = FastAPI(
    title="SOC L1 Agent",
    description="Local MVP for L1 SOC Automation",
    version="0.1"
)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "agent": "L1 SOC Agent",
        "mode": "local"
    }