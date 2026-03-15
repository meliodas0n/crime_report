import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [multipliedNum, setMultipliedNum] = useState(0)
  const [num, setNum] = useState(0)
  return (
    <>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <label>Enter a number: </label>
        <input type="number" value={num} onChange={(e) => setNum(Number(e.target.value))}></input>
        <button onClick={() => setMultipliedNum((count * num))}>
          Mutiplied number is {multipliedNum}
        </button>
      </div>
    </>
  )
}

export default App
