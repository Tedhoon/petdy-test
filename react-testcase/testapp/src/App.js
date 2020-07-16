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
  const [target, setTarget] = useState([]);
  const [data, setData] = useState([
      {
          "item": "칼로리",
      },
      {
          "item": "수분량",
      },
      {
          "item": "조단백",
      },
      {
          "item": "조지방",
      },
      {
          "item": "조섬유",
      },
      {
          "item": "조회분",
      },
      {
          "item": "칼슘",
      },
      {
          "item": "인",
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

    // 넣을껀 target id를 가진 하나의 것이다.
    const { 
      name,
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
    console.log(data)

    let tempData = data

    console.log(tempData[0])
    tempData[0][name] = parseFloat(calorie)
    tempData[1][name] = parseFloat(moisture)
    tempData[2][name] = parseFloat(crude_protein)
    tempData[3][name] = parseFloat(crude_fat)
    tempData[4][name] = parseFloat(crude_fiber)
    tempData[5][name] = parseFloat(crude_ash)
    tempData[6][name] = parseFloat(calcium)
    tempData[7][name] = parseFloat(phosphorus)
    console.log(tempData)
    setData(tempData)
    setTarget([name])
    console.log(target)
    // console.log(tempData[0])
    tempData = null



    for (let i=0; i<data.length; i++) {
      
        // console.log(calorie, moisture, phosphorus)
      // console.log(data[i])
      // tempData[i][feed[1].name] = parseFloat(feed[i][i])
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
    console.log(target)
  }, [data, target])
  const useHandleNutrientData = (event) => {
    const { id } = event.target;
    console.log(id)
    // setData(returnedData)
  };


  return (
    <div className="App">
      {/* <Graph/> */}
      <div style={tempStyle}>
        <NoviGraph data={data} target={target} />
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
