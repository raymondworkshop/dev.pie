import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import axios from "axios";


function App() {
  const [tasks, setTasks] = useState(0);

  useEffect(() => {
    axios.get('/api/v1.0/tasks')
      .then((response) => {
      
      const res = response.data;
      //{tasks: Array(1)} 
      console.log(res);
      //console.log(res["tasks"][0]);
      
        setTasks({
          id: res["tasks"][0].id,
          title: res["tasks"][0].title,
          description: res["tasks"][0].description,
          done: res["tasks"][0].done,
        }); 
      
    });

  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Tasks:
          <p>{tasks.title} : {tasks.description} </p>
        </a>
      </header>
    </div>
  );
}



export default App;
