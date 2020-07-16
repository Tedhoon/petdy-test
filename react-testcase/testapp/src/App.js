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
  const [keys, setKeys] = useState([]);
  const [feedKey, setFeedKey] = useState([]);
  const [nutrientKey, setNutrientKey] = useState([]);
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

  const filterData = (type, id) => {
    if (type==="feed") {
      return feed.filter(object => {
        return object['id'] === parseInt(id)
      })
    } else if (type==="nutrient") {
      return nutrient.filter(object => {
        return object['id'] === parseInt(id)
      })
    }
  }

  const useHandleFeedData = async(event) => {
    const { id } = event.target;
    const targetFeedData = await filterData("feed", id)

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
    
    // console.log("cal" , calorie)
    // console.log(data)

    let tempData = data

    if (tempData[0].hasOwnProperty(name)) {
      // key 값이 있는지 확인
      for(let i=0; i<tempData.length; i++) {
        delete tempData[i][name]
      }
    } else {
      tempData[0][name] = parseFloat(calorie)
      tempData[1][name] = parseFloat(moisture)
      tempData[2][name] = parseFloat(crude_protein)
      tempData[3][name] = parseFloat(crude_fat)
      tempData[4][name] = parseFloat(crude_fiber)
      tempData[5][name] = parseFloat(crude_ash)
      tempData[6][name] = parseFloat(calcium)
      tempData[7][name] = parseFloat(phosphorus)
    }

    // console.log(tempData[0])
    // tempData[0][name] = parseFloat(calorie)
    // tempData[1][name] = parseFloat(moisture)
    // tempData[2][name] = parseFloat(crude_protein)
    // tempData[3][name] = parseFloat(crude_fat)
    // tempData[4][name] = parseFloat(crude_fiber)
    // tempData[5][name] = parseFloat(crude_ash)
    // tempData[6][name] = parseFloat(calcium)
    // tempData[7][name] = parseFloat(phosphorus)
    // console.log(tempData)
    setData(tempData)
    setFeedKey([name])
    // console.log(target)
    // console.log(tempData[0])
    // tempData = null
  };
 

  const useHandleNutrientData = async(event) => {
    // 여기서 setData로 초기화?
    const { id } = event.target;
    const targetNutrientData = await filterData("nutrient", id)

    console.log(targetNutrientData)

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
    } = targetNutrientData[0];
    
    // console.log("cal" , calorie)
    // console.log(data)

    let tempData = data

    if (tempData[0].hasOwnProperty(name)) {
      // key 값이 있는지 확인
      for(let i=0; i<tempData.length; i++) {
        delete tempData[i][name]
      }
    } else {
      tempData[0][name] = parseFloat(calorie)
      tempData[1][name] = parseFloat(moisture)
      tempData[2][name] = parseFloat(crude_protein)
      tempData[3][name] = parseFloat(crude_fat)
      tempData[4][name] = parseFloat(crude_fiber)
      tempData[5][name] = parseFloat(crude_ash)
      tempData[6][name] = parseFloat(calcium)
      tempData[7][name] = parseFloat(phosphorus)
    }
    // console.log(tempData)
    setData(tempData)
    setNutrientKey([name])
    // console.log(target)
    // console.log(tempData[0])
    // tempData = null
    
  };

  useEffect(() => {
    console.log("작동")
    console.log(data)
    console.log(keys)
    let mergeKeys = new Array();
    mergeKeys = mergeKeys.concat(feedKey, nutrientKey)
    setKeys(mergeKeys)
  }, [data, feedKey, nutrientKey])



  return (
    <div className="App">
      {/* <Graph/> */}
      <div style={tempStyle}>
        <NoviGraph data={data} keys={keys} />
      </div>
      <div>
        {feed && feed.map(data=> 
          <button key={data.id} id={data.id} onClick={useHandleFeedData}>{data.name}</button>)}
        <br />   <br />   <br />   <br />   <br />   
        
        {nutrient && nutrient.map(data=> 
          <button key={data.id} id={data.id} onClick={useHandleNutrientData}>{data.name}</button>)}
        <br />   <br />   <br />   <br />   <br />   
      </div>
    </div>
  );
}

export default App;
