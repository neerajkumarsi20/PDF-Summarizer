import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import SummaryDisplay from './components/SummaryDisplay';
import QuestionAnswer from './components/QuestionAnswer';
import './App.css';

function App() {
  const [summary, setSummary] = useState("");
  const [pdfUploaded, setPdfUploaded] = useState(false);

  return (
    <div className="app-container">
      <h1>📄 PDF Summarizer + Q&A Bot</h1>
      <p>Upload a PDF → Get summary → Ask questions from the PDF.</p>

      <FileUpload setSummary={setSummary} setPdfUploaded={setPdfUploaded} />

      {summary && <SummaryDisplay summary={summary} />}

      {pdfUploaded && <QuestionAnswer />}
    </div>
  );
}

export default App;
