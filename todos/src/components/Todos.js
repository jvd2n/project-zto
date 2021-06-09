import React, { useState } from 'react';

function Todo({ todo }) {
  return (
    <div className="todo">
      {todo.text}
    </div>
  );
};


const Todos = () => {
  const [todos, setTodos] = useState([
    { text: "Learn about React" },
    { text: "Meet friend for lunch" },
    { text: "Learn about Python"}
  ]);
  
  return(<>
    <h2>ToDoLists</h2>
    <div className="todo-list">
      {todos.map((todo, index) => (
        <Todo
          key={index}
          index={index}
          todo={todo}
        />
      ))}
    </div>
    <input onChange={e => setTodos(e.target.value)}/>
    <button onClick={() => setTodos('')}>Del</button>
  </>);
}

export default Todos