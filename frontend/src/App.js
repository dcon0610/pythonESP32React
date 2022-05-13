import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

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
    <div className="App">
      <header className="App-header">
        <p>
         this is the data returned: {post.message}
        </p>

      </header>
    </div>
  );
}

export default App;
