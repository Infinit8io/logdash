import React, { Component } from 'react'
import MachineComponent from './MachineComponent.js'
import $ from 'jquery';

const API_URL = "http://localhost:5000/"

class MachineContainer extends Component {

  constructor(props){
    super(props)
    this.state = {
      machines: []
    }
  }

  componentDidMount(){
    //Jquery seems the only lib who works here...
    $.get(API_URL+"machines")
      .done(data => this.setState({machines: data}))
      .fail(ex => console.log(ex))
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
