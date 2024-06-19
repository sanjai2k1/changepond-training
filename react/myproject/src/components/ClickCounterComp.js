import React, { Component } from 'react'
import { HOCComp } from './HOCComp'

export  class ClickCounterComp extends Component {
  
  render() {
    return (
      <div>
        <p>Count is : {this.props.count}</p>
        <button onClick={()=>this.props.increment()}>Increment on click</button>
      </div>
    )
  }
}


export default HOCComp(ClickCounterComp)
