import React, { useEffect, useState } from 'react';
import './App.css';
import Graph from './Components/Graph';
import NoviGraph from './Components/Novi';
import { useFetchData } from './Hooks/useFetchData';
// import { useHandleData } from './Hooks/useHandleData';



const tempStyle={
  height:"93vh"
}

function App() {
  const [feed, nutrient] = useFetchData();
  const [data, setData] = useState([
      {
          "item": "칼로리",
          "타겟1": 0,
          "타겟2": 0,
      },
      {
          "item": "수분량",
          "타겟1": 0,
          "타겟2": 0,
      },
      {
          "item": "조단백",
          "타겟1": 0,
          "타겟2": 0,
      },
      {
          "item": "조지방",
          "타겟1": 0,
          "타겟2": 0,
      },
      {
          "item": "조섬유",
          "타겟1": 0,
          "타겟2": 0,
      },
      {
          "item": "조회분",
          "타겟1": 0,
          "타겟2": 0,
      },
      {
          "item": "칼슘",
          "타겟1": 0,
          "타겟2": 0,
      },
      {
          "item": "인",
          "타겟1": 0,
          "타겟2": 0,
      },

  ])

  const filterFeedData = (id) => {
    // if (feed || nutrient === null) {
    //     console.log("ERROR! Data is null")
    //     return;
    // }
    
    //여기서 if/else로 분기해서 data filtering?

    return feed.filter(object => {
        return object['id'] === parseInt(id)
    })
  }

  const useHandleFeedData = async(event) => {
    const { id } = event.target;
    const targetFeedData = await filterFeedData(id)

    console.log(targetFeedData)

    const tempData = data
    // 넣을껀 target id를 가진 하나의 것이다.
    let { 
      calorie,
      moisture,
      crude_protein,
      crude_fat,
      crude_fiber,
      crude_ash,
      calcium,
      phosphorus
    } = targetFeedData[0];
    
    console.log("cal" , calorie)

    for (let i=0; i<data.length; i++) {
      
        // console.log(calorie, moisture, phosphorus)
      // console.log(data[i])
      tempData[i][feed[1].name] = parseFloat(feed[i][i])
    }
    // console.log(tempData)
    // setData(...data, tempData)

    // return [data]
    // setData(returnedData)
    // let a = [data, ...tempData]
    // console.log(a)
    
  };
  useEffect(() => {
    console.log("작동")
    console.log(data)
  }, [data])
  const useHandleNutrientData = (event) => {
    const { id } = event.target;
    console.log(id)
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
          <button key={data.id} id={data.id} onClick={useHandleFeedData}>{data.name}</button>)}
        <br />   <br />   <br />   <br />   <br />   
        
        {nutrient && nutrient.map(data=> 
          <button key={data.id} id={data.id} onClick={useHandleNutrientData}>{data.name}</button>)}
        <br />   <br />   <br />   <br />   <br />   
        {data.map(data=>
          <button>{data.item}</button>)}
      </div>
    </div>
  );
}

export default App;
