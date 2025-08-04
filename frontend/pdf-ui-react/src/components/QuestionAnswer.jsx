import React, { useState } from 'react';
import axios from 'axios';

const QuestionAnswer = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [source, setSource] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question) return;

    setLoading(true);
    try {
      const res = await axios.post("http://localhost:8000/ask-question/", {
        question,
        model: "deepset/roberta-base-squad2"
      });
      setAnswer(res.data.answer);
      setSource(res.data.source);
    } catch (err) {
      alert("Failed to fetch answer.");
    }
    setLoading(false);
  };

  return (
    <div className="qa-box">
      <h3>Ask a question from the PDF</h3>
      <input
        type="text"
        placeholder="E.g. What is the conclusion?"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button onClick={askQuestion} disabled={loading}>
        {loading ? "Searching..." : "Ask"}
      </button>

      {answer && (
        <div>
          <h4>Answer:</h4>
          <p>{answer}</p>
          <h5>Source Context:</h5>
          <pre>{source}</pre>
        </div>
      )}
    </div>
  );
};

export default QuestionAnswer;
