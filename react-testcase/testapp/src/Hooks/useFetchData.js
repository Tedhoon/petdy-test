import React, { useState, useEffect } from "react";
import axios from "axios";
import { BACKEND } from '../config';


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
            const result = await axios.get(`${BACKEND}/exchangedfeed/`)
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
    const [data, setData] = useState([
        {
            "item": "칼로리",
            "타겟1": 10,
            "타겟2": 10,
        },
        {
            "item": "수분량",
            "타겟1": 20,
            "타겟2": 30,
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

    useEffect(() => {
        getFeedAxios();
        console.log("export할 data : ", data)
    }, [data])



    return [feed,data]
}