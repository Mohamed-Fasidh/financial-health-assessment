import React, { useState } from "react";
import { analyze, uploadFile } from "../services/api";

export default function Dashboard() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [file, setFile] = useState(null);

  const handleAnalyze = async () => {
    setLoading(true);
    try {
      let res;

      // If file uploaded → call upload API
      if (file) {
        res = await uploadFile(file);
      } else {
        // fallback demo analysis
        res = await analyze();
      }

      setResult(res);
    } catch (err) {
      console.error(err);
      alert("Failed to analyze financial health");
    } finally {
      setLoading(false);
    }
  };

  const getScoreClass = (score) => {
    if (score < 40) return "low";
    if (score < 70) return "medium";
    return "high";
  };

  return (
    <div className="app-container">
      <div className="card">
        <h1>Financial Health</h1>

        {/* ===== Styled File Upload ===== */}
        <div className="file-upload">
          <input
            id="fileInput"
            type="file"
            accept=".csv,.xlsx,.pdf"
            hidden
            onChange={(e) => setFile(e.target.files[0])}
          />

          <label htmlFor="fileInput" className="file-btn">
            Choose File
          </label>

          <span className="file-name">
            {file ? file.name : "No file chosen"}
          </span>
        </div>

        {/* ===== Analyze Button ===== */}
        <button
          className="btn"
          onClick={handleAnalyze}
          disabled={loading}
        >
          {loading ? "Analyzing..." : "Analyze"}
        </button>

        {/* ===== Result ===== */}
        {result && (
          <div className="result">
            <div className={`score ${getScoreClass(result.score)}`}>
              Score: {result.score}
            </div>
            <p><b>Working Capital:</b> ₹{result.working_capital}</p>
            <p><b>Loan Recommendation:</b> {result.recommendation}</p>
            <div className="insight">{result.insights}</div>
          </div>
        )}
      </div>
    </div>
  );
}
