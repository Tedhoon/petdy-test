import React from 'react';
import './App.css';
import Graph from './Components/Graph';
import NoviGraph from './Components/Novi';


const tempStyle={
  height:"98vh"
}

function App() {
  return (
    <div className="App">
      <div style={tempStyle}>
        <NoviGraph />
      </div>
    </div>
  );
}

export default App;
