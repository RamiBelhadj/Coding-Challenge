import React from 'react'
import './App.css'
import ExpandableContainer from './components/ExpandableContainer'
import InputData from '../input-task-1.json';

import RecursiveContainer from './components/RecursiveContainer';

function App() {
  
  return (
      <div className="h-screen w-96 border-r p-4">
        <span className="text-lg font-bold w-full">Menu:</span>
        <div>Your component here! <br/>
          <RecursiveContainer data={InputData}></RecursiveContainer>
        </div>
      </div>
      
  
  )
}

export default App
