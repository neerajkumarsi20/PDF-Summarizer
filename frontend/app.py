import streamlit as st
import requests

st.title("📄 PDF Summarizer + Q&A Bot")
st.write("Upload a PDF → Get summary → Ask questions from the PDF.")

pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

model_choice = st.selectbox("Choose Summary Model", [
    "facebook/bart-large-cnn",
    "google/pegasus-cnn_dailymail",
    "sshleifer/distilbart-cnn-12-6",
    "csebuetnlp/mT5_multilingual_XLSum", # multilingual summarizer
    "philschmid/bart-large-cnn-samsum",  # optimized for dialogue / meetings
    "Falconsai/text_summarization"      # modern FLAN-T5-based summarizer

])

st.markdown("### 🛠️ Customize Summary Length")
min_len = st.slider("Minimum Summary Length", 50, 500, 100, step=10)
max_len = st.slider("Maximum Summary Length", min_len + 50, 1000, 300, step=10)


if pdf_file:
    with st.spinner("Summarizing..."):
        response = requests.post(
            "http://localhost:8000/summarize-pdf/",
            params={
        "model": model_choice,
        "min_length": min_len,
        "max_length": max_len
    },
            files={"file": pdf_file},
        )
        if response.status_code == 200:
            st.subheader("Summary:")
            st.success(response.json()["summary"])
        else:
            st.error("Summarization failed.")

    st.markdown("---")

    st.subheader("Ask a question from the PDF")

    question = st.text_input("Type your question below 👇")
    if question:
        with st.spinner("Searching answer..."):
            response = requests.post(
                "http://localhost:8000/ask-question/",
                json={"question": question, "model": "deepset/roberta-base-squad2"},
            )
            if response.status_code == 200:
                res_json = response.json()
                st.success(res_json["answer"])
                st.markdown("**Source Context:**")
                st.info(res_json["source"])
            else:
                st.error("Failed to fetch answer.")


    
