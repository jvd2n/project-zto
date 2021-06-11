import { createStore } from 'redux';
import todoReducer from './todo.reducer';
export { default as todoReducer } from './todo.reducer';
// export const store = createStore(todoReducer)
export const store = createStore(todoReducer)