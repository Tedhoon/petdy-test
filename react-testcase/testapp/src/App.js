import React, { useEffect, useState } from 'react';
import './App.css';
import Graph from './Components/Graph';
import NoviGraph from './Components/Novi';
import { useFetchData } from './Hooks/useFetchData';




const tempStyle={
  height:"93vh"
}

function App() {
  const [feed, mydata] = useFetchData();
  const [data, setData] = useState(mydata);
  const checkTarget = () => {
    // const returnedData = useHandleData()
    // setData(returnedData)
  };


  return (
    <div className="App">
      {/* <Graph/> */}
      <div style={tempStyle}>
        <NoviGraph data={data} />
      </div>
      <div>
        {feed && feed.map(data=> 
          <button>{data.name}</button>)}
        <br />
        {mydata && mydata.map(data=>
          <button>{data.item}</button>)}
      </div>
    </div>
  );
}

export default App;
