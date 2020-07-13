import React, { useEffect, useState, useCallback } from "react";
import { Chart } from 'react-chartjs-2';
import { BACKEND } from '../config';
import axios from 'axios';

const useGraph = () => {
    useEffect(() => {
        // 우선 컨텍스트를 가져옵니다. 
        const ctx = document.getElementById("myChart").getContext('2d');
        /*
        - Chart를 생성하면서, 
        - ctx를 첫번째 argument로 넘겨주고, 
        - 두번째 argument로 그림을 그릴때 필요한 요소들을 모두 넘겨줍니다. 
        */
        const baseChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ["급여량", "수분량", "조단백", "조지방", "조섬유", "조회분", "칼슘", "인"],
                datasets: [{
                    label: 'Essential Nutrients',
                    data: [12, 19, 3, 5, 2, 3, 10, 9],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                maintainAspectRatio: true, // default value. false일 경우 포함된 div의 크기에 맞춰서 그려짐.
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                }
            }
        });
    }, [])
    }


const mockAsyncNutrientData = () => 
    new Promise(resolve => {
        setTimeout(async function() {
            const result = await axios.get(`${BACKEND}/feed/`)
            resolve({
                data: result.data
            })
        }, 200)
    })


const useDataGraph = (graphData) => {
    useEffect(() => {
        // 우선 컨텍스트를 가져옵니다. 
        const ctx = document.getElementById("customChart").getContext('2d');
        /*
        - Chart를 생성하면서, 
        - ctx를 첫번째 argument로 넘겨주고, 
        - 두번째 argument로 그림을 그릴때 필요한 요소들을 모두 넘겨줍니다. 
        */
        const baseChart2 = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ["급여량", "수분량", "조단백", "조지방", "조섬유", "조회분", "칼슘", "인"],
                datasets: [{
                    label: 'Essential Nutrients',
                    data: graphData,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                maintainAspectRatio: true, // default value. false일 경우 포함된 div의 크기에 맞춰서 그려짐.
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                }
            }
        });
    }, [graphData])
}


function Graph () {
    const [nutrientData, setNutrientData] = useState(null);
    const [graphData, setGraphData] = useState([0,0,0,0,0,0,0,0]);
    useGraph();

    const getNutrientData = useCallback(async () => {
        try {
            const { data } = await mockAsyncNutrientData();
            setNutrientData(data);
            console.log(data)
        } catch (err) {
            console.error(err);
        }
      },[nutrientData]);
      
    useEffect(() => {
        getNutrientData();
    }, [])

    useDataGraph(graphData);
    
    const filterNutrientData = (id) => {
        if (nutrientData === null) {
            console.log("ERROR! nutrientData is null")
            return;
        }

        return nutrientData.filter(object => {
            return object['id'] === parseInt(id)
        })

    }
    const applyNutrient = async (event) => {
        const { id } = event.target; 
        const object = await filterNutrientData(id)
        console.log(object)
        const { calorie, moisture, crude_protein, crude_fat, crude_fiber, crude_ash, calcium, phosphorus } = object[0];
        setGraphData([calorie/100, moisture, crude_protein, crude_fat, crude_fiber, crude_ash, calcium, phosphorus])
    }

    return (
        <>
            <div style={{width: "50vw"}}>
                <canvas id="myChart"></canvas>
            </div>

            <div style={{width: "50vw"}}>
                <canvas id="customChart"></canvas>
            </div>

            {nutrientData && nutrientData.map((data) => 
                
                <div onClick={applyNutrient} id={data.id} key={data.id} style={{border: "1px solid black"}}>
                    {data.name}
                </div>
            )}
        </>
    )
}

export default Graph;


// 이제 y축을 하루 기준 필요 섭취량 100% 기준으로 나타내고
// 사료, 영양제 탭으로 나눌까
// 클릭시 axios요청으로 백엔드에서 