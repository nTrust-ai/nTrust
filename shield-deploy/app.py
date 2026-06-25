from fastapi import FastAPI
import uvicorn

app = FastAPI(title="ThreatShield AI", version="1.0.0")

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "ntrust-api", "tls": "TLSv1.3"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9090)
