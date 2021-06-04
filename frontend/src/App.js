import React from 'react';
import { BrowserRouter as Router, Link } from "react-router-dom"
import styled from 'styled-components';
import Counter from './counter/Counter'
import Login from 'user/Login'
import SignUp from './user/SignUp'
import UserDetail from './user/UserDetail'
import UserEdit from 'user/UserEdit'
import UserList from 'user/UserList'

const App = () => {
  return (<>
      <nav>
        <Router>
          <Link to="/">Home</Link><br/>
          <Link to="/">Blog</Link><br/>
          <Link to="/">About Me</Link><br/>
          <Link to="">Go to Google</Link><br/>
        </Router>
      </nav>

      <Counter/>
      <Login/>
      <SignUp/>
      <UserDetail/>
      <UserEdit/>
      <UserList/>
    </>)
}
const Container = styled.div`
  width: 100%;
  border: 1px solid #d1d8e4;
`
const Element = styled.div`
  width: 400px;  
  margin: 0 auto;
`
export default App