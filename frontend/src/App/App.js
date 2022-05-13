import React from 'react';
import logo from './../logo.svg';
import './App.css';
import axios from 'axios';
import Navbar from './../Components/navbar'


const baseURL = "/api/test"
function App() {
 const [post, setPost] = React.useState("");

 React.useEffect(() => {
   axios.get(baseURL).then((response) => {
    console.log("Response:", response);
   setPost(response.data);
   
 });
},[]);
  return (

      
      <div>
        <Navbar/>
        <div> Data is: {post.message}</div>
        
      </div>

  );
}

export default App;
