import React, { useState, useRef } from 'react';

// const tasks = [
//   { 
//     id: 1,
//     name: "task1", 
//     done: false 
//   },
// ];

const Todo = () => {
  const [item, setItem] = useState('')
  return(<>
    <h2>할일 목록</h2>
    <h4>{item}</h4>
    <input onChange={ e => setItem(e.target.value) }/>
    <button onClick={ () => { setItem('') } }>Add</button>
    <button onClick={ () => { setItem('') } }>Del</button>
  </>)
}

export default Todo