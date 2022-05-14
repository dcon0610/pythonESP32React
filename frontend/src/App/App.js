import React from 'react';
import './App.css';
import Navbar from './../Components/navbar'
import Plot from './../Components/plotly'
import Api from './../Utils/Api'



function App() {
 const [post, setPost] = React.useState("");

 React.useEffect(() => {
   Api.test().then((response) => {
    console.log("Response:", response);
   setPost(response.data);
   
 });
},[]);
  return (

      
      <div>
        <Navbar/>
        <Plot/>
        
      </div>

  );
}

export default App;
