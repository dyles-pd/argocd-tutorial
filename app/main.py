from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI ArgoCD Demo"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/version")
async def version():
    return {"version": "2.0.0", "updated_by": "tekton"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
