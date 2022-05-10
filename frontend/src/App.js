import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

const baseURL = "http://127.0.0.1:9566/test"
function App() {
 const [post, setPost] = React.useState("");

 React.useEffect(() => {
   axios.get(baseURL).then((response) => {
    console.log("Response:", response);
   setPost(response);
   
 });
},[]);
  return (
    <div className="App">
      <header className="App-header">
        <p>
         this is the data returned: {post.data}
        </p>

      </header>
    </div>
  );
}

export default App;
