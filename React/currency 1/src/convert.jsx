import React, { useState } from "react";
import { currencies } from "./data";

const Convert = () => {
  const [amount, setAmount] = useState(0);
  const [error, setError] = useState("");
  const handleOnChange = (e) => {
    setAmount(e.target.value);
    if (isNaN(e.target.value)) {
      setError("Please enter a valid amount");
    } else {
      setError("");
    }
  };
  return (
    <>
      <div className="input">
        <div className="form-input">
          <label htmlFor="">From</label>
          <select>
            <option value="USD">USD - US Dollar</option>
          </select>
        </div>
        <div className="form-input">
          <label htmlFor="">To</label>
          <select>
            {currencies.map((cur) => (
              <option value={cur.iso}>
                {cur.iso} - {cur.label}
              </option>
            ))}
          </select>
        </div>
        <div className="form-input">
          <label htmlFor="">Amount</label>
          <div className="amount">
            <span>$</span>
            <input value={amount} onChange={handleOnChange} type="text" />
          </div>
          {error ? <p className="error">{error}</p> : null}
        </div>
      </div>
      <button>Convert</button>
    </>
  );
};

export default Convert;
