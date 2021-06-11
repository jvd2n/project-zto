import React from 'react';
import { Redirect, Route, BrowserRouter as Router } from "react-router-dom";
import { Login, Signup, UserDetail, UserList, UserEdit } from 'user/index'
import { Nav } from 'common'
import { Home, User, Item } from 'templates'
import { Counter } from 'counter'
import { Provider } from 'react-redux';
import { combineReducers, createStore } from 'redux';
import { todoReducer } from './store'
import { Schedule } from 'todos/containers';

const rootReducer = combineReducers({todoReducer});

const App = () => {
  return (<div>
    <Router>
      <Provider store = {createStore(rootReducer)}>
        <Nav/>
        <Route exact path='/home' component={Home}/>
        <Redirect exact from={'/'} to={'/home'}/>
        <Route exact path='/counter' component={Counter}/>
        <Route exact path='/user' component={User}/>
        <Route exact path='/item' component={Item}/>
        <Route exact path='/login-form' component={Login}/>
        <Route exact path='/signup-form' component={Signup}/>
        <Route exact path='/user-detail' component={UserDetail}/>
        <Route exact path='/user-edit' component={UserEdit}/>
        <Route exact path='/user-list' component={UserList}/>
        <Route exact path='/todos' component={Schedule}/>
      </Provider>
    </Router>
  </div>)
}

export default App