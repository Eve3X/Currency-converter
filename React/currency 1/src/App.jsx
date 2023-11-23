import { CircleDollarSign } from "lucide-react";
import { LineChart } from "lucide-react";
import { useState } from "react";
import Convert from "./convert";
import Charts from "./charts";

function App() {
  const [tab, setTab] = useState(0);
  return (
    <div className="App">
      <div className="header">
        <h1>Currency Converter</h1>
        <h3>Check live foreign currency exchange rates</h3>
      </div>
      <div className="container">
        <div className="row">
          <div
            onClick={() => setTab(0)}
            className={`column ${tab === 0 ? "active" : ""}`}
          >
            <span>
              <CircleDollarSign />
              Convert
            </span>
          </div>
          <div
            onClick={() => setTab(1)}
            className={`column ${tab === 1 ? "active" : ""}`}
          >
            <span>
              <LineChart />
              Charts
            </span>
          </div>
        </div>
        {tab === 0 ? <Convert></Convert> : null}
        {tab === 1 ? <Charts></Charts> : null}
      </div>
    </div>
  );
}

export default App;
