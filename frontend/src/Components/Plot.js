import React, { useEffect, useState } from 'react';
import Plotly from 'plotly.js-basic-dist-min'
import createPlotlyComponent from "react-plotly.js/factory";
import styles from './Plot.module.css'
import Api from '../Utils/Api'

import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

const Plot = createPlotlyComponent(Plotly);
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
    <div>
        <Row>
        <Col xs="1">
            </Col>
            <Col xs="11">
            <Plot className={styles.plot}
            data={[
                {
                x: tempData.date,
                y: tempData.temperature,
                type: 'scatter',
                mode: 'lines',
                marker: {color: 'blue'},
                }
            ]}
            layout={{ title: 'Green house temperature'}} />
            </Col>
            

        </Row>
    </div>

)

}
export default Plotlygraph;