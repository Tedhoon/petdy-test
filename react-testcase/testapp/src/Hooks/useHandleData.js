import React, { useState, useEffect } from "react";
import { BACKEND } from '../config';





const filterData = (id) => {
    if (nutrientData === null) {
        console.log("ERROR! nutrientData is null")
        return;
    }

    return nutrientData.filter(object => {
        return object['id'] === parseInt(id)
    })
}




export const useHandleData = async(event) => {
    const { id } = event.target; 
    const object = await filterData(id)
    console.log(object)
    
    return returnedData 
}