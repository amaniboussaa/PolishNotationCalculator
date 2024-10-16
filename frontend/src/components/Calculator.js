import React, { useState } from 'react';
import axios from 'axios';
import './Calculator.css'; // Ensure to include your CSS file

const API_URL = process.env.REACT_APP_API_URL;


const Calculator = () => {
  const [operation, setOperation] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  const validateExpression = (expression) => {
    const regex = /^[0-9\s\+\-\*\/]+$/; // Basic validation for NPI expressions
    return regex.test(expression);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!validateExpression(operation)) {
      setError("Veuillez entrer une expression valide.");
      setResult(null);
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await axios.post(`${API_URL}/calculate/`, { 
        expression: operation  
      });

      setResult(response.data.result);
      setHistory([...history, { operation, result: response.data.result }]);
      setOperation(""); // Clear input field after submission
    } catch (err) {
      console.error(err);
      setError("Erreur dans l'opération. Veuillez réessayer.");
      setResult(null);
    } finally {
      setLoading(false);
    }
  };

  const handleExport = async () => {
    try {
        const response = await axios.get(`${API_URL}/export/`, {
        responseType: 'blob', // Important for handling CSV files
      });

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'operations.csv'); // Specify the file name
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link); // Clean up the link element
    } catch (error) {
      console.error("Failed to export CSV:", error);
    }
  };

  return (
    <div className="calculator">
      <h1>Calculatrice NPI</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={operation} 
          onChange={(e) => setOperation(e.target.value)} 
          placeholder="Entrez une expression NPI (e.g. 2 3 +)" 
          className="calculator-input" 
          onKeyPress={(e) => e.key === 'Enter' && handleSubmit(e)} // Submit on Enter key press
        />
        <button type="submit" className="calculator-button" disabled={loading}>
          {loading ? "Calcul en cours..." : "Calculer"}
        </button>
      </form>
      {result !== null && <h2 className="calculator-result">Résultat: {result}</h2>}
      {error && <p className="error">{error}</p>}
      <History history={history} />
      <button className="export-button" onClick={handleExport}>
        Exporter en CSV
      </button>
    </div>
  );
};

// History Component
const History = ({ history }) => {
  return (
    <div className="history">
      <h3>Historique des Calculs</h3>
      {history.length === 0 ? (
        <p>Aucun calcul effectué.</p>
      ) : (
        <ul>
          {history.map((item, index) => (
            <li key={index}>
              <strong>{item.operation}</strong> = {item.result}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Calculator;
