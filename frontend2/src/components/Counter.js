import React, { useState } from 'react';

const Counter = () => {

  const [count, setCount] = useState(0)

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 2)}>++</button>
      <button onClick={() => setCount(count + 1) }> + </button>
      <button onClick={() => setCount(count - 1) }> - </button> 
      <button onClick={() => setCount(count - 2)}>--</button>
    </div>
  )
}

export default Counter