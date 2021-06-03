import React from 'react'
import { Link } from 'react-router-dom'
import styled from 'styled-components'

const App = () => {
  return (
  <>
  <nav>
    <Link to="/">Home</Link>
    <Link to="/">Blog</Link>
    <Link to="/">About Me</Link>
  </nav>

  <h1>첫 번째 크기 헤드라인</h1>
  <h2>두 번째 크기 헤드라인</h2>
  <h3>세 번째 크기 헤드라인</h3>
  <h4>네 번째 크기 헤드라인</h4>
  <h5>다섯 번째 크기 헤드라인</h5>
  <p>문단은 p로 쓰세요. p는 Paragraph의 앞글자</p>
  <Link to="https://www.google.com">Go to Google</Link>
  <hr/>
  <img src="/" width="600px"></img>
  </>
  )
}

export default App