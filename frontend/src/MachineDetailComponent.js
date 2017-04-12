import React, { Component } from 'react'

class MachineDetailComponent extends Component {

  constructor(props){
    super(props)
    this.state = {
      name: props.name
    }
  }

  componentDidMount(){

  }
  render(){
    return (
      <div>Hello from detail {this.state.name}</div>
    )
  }
}
export default MachineDetailComponent;
