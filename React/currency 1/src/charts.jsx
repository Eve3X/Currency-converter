import React from "react";
import { currencies } from "./data";

const charts = () => {
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
      </div>
      <button>View Chart</button>
    </>
  );
};

export default charts;
