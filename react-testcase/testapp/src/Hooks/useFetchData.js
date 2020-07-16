import React, { useState, useEffect } from "react";
import axios from "axios";
import { BACKEND } from '../config';
// 추후 React.memo 최적화하기

// data를 fetch후 가공해서 알맞은 format으로 바꿔주는 hook

// [{
//     "nutrient": "",
//     "타겟1: "값",
// /
//     "타겟2: "값",
// /     ...
//     }
//     ...  
// ]

// "사료이름" : 값,
// "영양제이름": 값

const mockAsyncFeedData = () => 
    new Promise(resolve => {
        setTimeout(async function() {
            const result = await axios.get(`${BACKEND}/exchangedfeed/`)
            resolve({
                data: result.data
            })
        }, 100)
    })

const mockAsyncNutrientData = () => 
    new Promise(resolve => {
        setTimeout(async function() {
            const result = await axios.get(`${BACKEND}/exchangednutrient/`)
            resolve({
                data: result.data
            })
        }, 100)
    })

export const useFetchData = () => {
    // 일단 data에 feed만 담아서 해봅시당 
    // data는 object여야 함
    // data는 Memo에 넣어주기!
    const [feed, setFeed] = useState(null)
    const [nutrient, setNutrient] = useState(null)

    // mockAsyncData 호출 및 데이터 set
    const getFeedAxios = async () => {
        try {
            const { data : fetchedData } = await mockAsyncFeedData();
            setFeed(fetchedData);
            console.log("fetched feed data", fetchedData)
        } catch (err) {
            console.error(err);
        }
      };


    const getNutrientAxios = async () => {
        try {
            const { data : fetchedData } = await mockAsyncNutrientData();
            setNutrient(fetchedData);
            console.log("fetched nutrient data", fetchedData)
        } catch (err) {
            console.error(err);
        }
      };


    useEffect(() => {
        getFeedAxios();
        getNutrientAxios();
        // console.log("export할 data : ", data)
    }, [])



    return [feed, nutrient]
}