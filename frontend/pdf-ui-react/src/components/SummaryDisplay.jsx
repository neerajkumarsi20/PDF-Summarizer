import React from 'react';

const SummaryDisplay = ({ summary }) => {
  return (
    <div className="summary-box">
      <h2>Summary</h2>
      <p>{summary}</p>
    </div>
  );
};

export default SummaryDisplay;
