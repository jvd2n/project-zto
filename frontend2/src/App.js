// import logo from './logo.svg';
import './App.css';
import { Route } from "react-router-dom";
import { Counter } from 'components/index';

function App() {
  return (
    <div>
      <Route exact path='/counter' component={Counter}/>
    </div>
  );
}

export default App;
