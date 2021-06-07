import React from 'react';
import { Route } from "react-router-dom";
import styled from 'styled-components';
import { Counter } from 'counter/index'
import { Login, Signup, UserDetail, UserList, UserEdit } from 'user/index'
import { Home } from 'common/index'

const App = () => {
  return (<div>
      <Route exact path='/' component={Home}/>
      <Route exact path='/counter' component={Counter}/>
      <Route exact path='/login' component={Login}/>
      <Route exact path='/signup' component={Signup}/>
      <Route exact path='/user-detail' component={UserDetail}/>
      <Route exact path='/user-edit' component={UserEdit}/>
      <Route exact path='/user-list' component={UserList}/>
  </div>)
}
// const Container = styled.div`
//   width: 100%;
//   border: 1px solid #d1d8e4;
// `
// const Element = styled.div`
//   width: 400px;  
//   margin: 0 auto;
// `
export default App