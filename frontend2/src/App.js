// import logo from './logo.svg';
import './App.css';
import { Route } from "react-router-dom";
import { Counter, TodoInput } from 'components/index';
import { Schedule } from 'containers/index'

function App() {
  return (
    <div>
      <Route exact path='/' component={Schedule}/>
      <Route exact path='/todo' component={TodoInput}/>
      <Route exact path='/counter' component={Counter}/>
    </div>
  );
}

export default App;
