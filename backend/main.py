from fastapi import FastAPI, UploadFile, File, Request, Form
import fitz
from summarizer import summarize_text
from qa import answer_question
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store extracted PDF text globally
pdf_text_store = {"text": ""}

def extract_text_from_pdf(file) -> str:
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text

@app.post("/summarize-pdf/")
async def summarize_pdf(
    request: Request,
    file: UploadFile = File(...),
):
    model = request.query_params.get("model", "facebook/bart-large-cnn")
    min_length = int(request.query_params.get("min_length", 100))
    max_length = int(request.query_params.get("max_length", 300))

    text = extract_text_from_pdf(file.file)
    pdf_text_store["text"] = text
    summary = summarize_text(text, model, min_length, max_length)
    return {"summary": summary}


@app.post("/ask-question/")
async def ask_question(request: Request):
    data = await request.json()
    question = data.get("question", "")
    model = data.get("model", "deepset/roberta-base-squad2")
    context = pdf_text_store.get("text", "")
    if not context:
        return {"answer": "❌ No PDF uploaded yet.", "source": "", "followups": []}

    result = answer_question(context, question, model)

    # Generate follow-up questions using same or different model
    

    return {
        "answer": result["answer"],
        "source": result["source"],
    }






