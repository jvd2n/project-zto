import React, { useState } from 'react';
import { useDispatch } from 'react-redux';  // Python으로 전달하는 Library
// import { useForm } from 'react-hook-form';
import { v4 as uuidv4 } from 'uuid';
import { addTodoAction } from 'store/todo.reducer'

const InputTodo = () => {
  const [ todo, setTodo ] = useState('');
  const dispatch = useDispatch();

  const submitForm = e => {
    e.preventDefault();
    console.log(`uuidv4 : ${uuidv4}`);
    const newTodo = {
      id: uuidv4(),
      name: todo,
      complete: false
    };
    addTodo(newTodo);
    setTodo('');
    console.log(newTodo);
  };

  const addTodo = todo => dispatch(addTodoAction(todo));

  const handleChange = e => {
    e.preventDefault();
    setTodo(e.target.value);
  };

  return(<>
  <h2>할일 목록</h2>
  <form onSubmit={submitForm} method='POST'>
    <div className="row mt-3">
      <div className="form-group col-sm-8">
        <input
          type="text"
          placeholder="할일 입력"
          name="todo"
          className="form-control"
          value={todo}
          onChange={handleChange}
        />
        {/* <button type='submit'>Submit Btn</button> */}
      </div>
    </div>
  </form>
  </>)
};

export default InputTodo;