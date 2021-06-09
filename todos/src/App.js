import { Route } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import { Todos } from './components/index';

function App() {
  return (
    <div>
      <Route exact path="/todos" component={Todos} />
    </div>
  );
}


export default App;
