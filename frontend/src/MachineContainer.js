import React, { Component } from 'react'
import MachineComponent from './MachineComponent.js'

class MachineContainer extends Component {

  constructor(props){
    super(props)
    this.state = {
      machines: []
    }
  }

  componentDidMount(){
    fetch('machines.json')
        .then(response => response.json())
        .then(data => this.setState({machines:data}))
  }
  render(){
    return (
      <div>
        <ol className="breadcrumb">
          <li className="breadcrumb-item active">Home</li>
        </ol>
        <div className="card-columns">
          {this.state.machines.map(data => <MachineComponent key={data.machine_mac} machine_info={data} />)}
        </div>
      </div>
    )
  }
}
export default MachineContainer;
