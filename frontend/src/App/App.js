import React from 'react';
import './App.css';
import Navbar from './../Components/navbar'
import Plot from '../Components/Plot'

import Container from 'react-bootstrap/Container'



function App() {

  return (

      
      <Container fluid >
        <Navbar/>
        <Plot/>
      </Container>

  );
}

export default App;
