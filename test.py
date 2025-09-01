from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Node/frontend to call FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

last_result = None

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are allowed")

    contents = await file.read()
    text = contents.decode("utf-8")

    try:
        numbers = [int(line.strip()) for line in text.splitlines() if line.strip()]
        incremented = [n + 1 for n in numbers]

        global last_result
        last_result = "\n".join(map(str, incremented))

        return {"original": numbers, "processed": incremented}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing file: {e}")

@app.get("/api/data")
def get_data():
    if last_result:
        return {"message": last_result}
    return {"message": "No file has been uploaded yet"}
