import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = ({ setSummary, setPdfUploaded }) => {
  const [file, setFile] = useState(null);
  const [model, setModel] = useState("facebook/bart-large-cnn");
  const [minLength, setMinLength] = useState(100);
  const [maxLength, setMaxLength] = useState(300);
  const [loading, setLoading] = useState(false);

  const models = [
    "facebook/bart-large-cnn",
    "google/pegasus-cnn_dailymail",
    "sshleifer/distilbart-cnn-12-6",
    "csebuetnlp/mT5_multilingual_XLSum",
    "philschmid/bart-large-cnn-samsum",
    "Falconsai/text_summarization"
  ];

  const handleSubmit = async () => {
    if (!file) return alert("Please upload a PDF.");

    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post(
        "http://localhost:8000/summarize-pdf/",
        formData,
        {
          params: { model, min_length: minLength, max_length: maxLength },
          headers: { "Content-Type": "multipart/form-data" },
        }
      );
      setSummary(res.data.summary);
      setPdfUploaded(true);
    } catch (err) {
      alert("Summarization failed.");
    }
    setLoading(false);
  };

  return (
    <div className="upload-box">
      <input type="file" accept="application/pdf" onChange={e => setFile(e.target.files[0])} />
      
      <label>Select Model:</label>
      <select value={model} onChange={e => setModel(e.target.value)}>
        {models.map((m) => <option key={m} value={m}>{m}</option>)}
      </select>

      <label>Min Summary Length: {minLength}</label>
      <input type="range" min="50" max="500" step="10" value={minLength} onChange={e => setMinLength(Number(e.target.value))} />

      <label>Max Summary Length: {maxLength}</label>
      <input type="range" min={minLength + 50} max="1000" step="10" value={maxLength} onChange={e => setMaxLength(Number(e.target.value))} />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Summarizing..." : "Submit"}
      </button>
    </div>
  );
};

export default FileUpload;
