import sys
import os
import json
from graph.graph import app as graph_app
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel


sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from graph.graph import app as graph_app


app = FastAPI()


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Virtual Herbal Garden API"}


@app.post("/ask")
def ask(question: Question):

    result = graph_app.invoke({
        "question": question.question
    })

    return {
        "question": question.question,
        "answer": result.get("answer"),
        "herbs": result.get("herbs"),
        "sources": result.get("docs")
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    content = await file.read()

    # ---------- Parse JSON safely ----------
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return {
            "status": "error",
            "message": "That file isn't valid JSON. Please check the formatting and try again."
        }

    # ---------- Accept either a list or a single object ----------
    if isinstance(data, dict):
        records = [data]
    elif isinstance(data, list):
        records = data
    else:
        return {
            "status": "error",
            "message": "JSON must be an object or a list of objects."
        }

    if len(records) == 0:
        return {
            "status": "error",
            "message": "The uploaded JSON file is empty."
        }

    # ---------- Chunk and store ----------
    try:
        from rag.splitter import make_chunks
        from rag.vector_store import add_chunks

        chunks = make_chunks(records)

        if len(chunks) == 0:
            return {
                "status": "error",
                "message": "No usable data was found in this file. Make sure each entry has at least a name and some fields."
            }

        add_chunks(chunks)

        return {
            "status": "success",
            "filename": file.filename,
            "plants_loaded": len(records),
            "chunks_created": len(chunks)
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to process file: {e}"
        }