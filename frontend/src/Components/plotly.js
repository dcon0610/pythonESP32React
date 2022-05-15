import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js'
import Api from './../Utils/Api'

const Plotlygraph = () => {

const [tempData, getTempData] = React.useState({date: [], temperature: [] }) 

useEffect(() => {
    Api.getTemperature()
        .then((response) => {
            console.log("response: ", response)
            getTempData({date: response.data.time, temperature: response.data.temperature});
            console.log("this is the temp data: ", tempData);
        })
        .catch(error => {
            console.log(error)
        })
    }, [])

return (
<Plot 
     data={[
        {
          x: tempData.date,
          y: tempData.temperature,
          type: 'scatter',
          mode: 'lines',
          marker: {color: 'blue'},
        }
      ]}
      layout={{ title: 'Green house temperature'}}
    />
)

}
export default Plotlygraph;