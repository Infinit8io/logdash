import React, { Component } from 'react'
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'

class MachineComponent extends Component {

  constructor(props){
    super(props)
    this.state = {
      machine_info: this.props.machine_info
    }
  }

  render(){
    return  (
      <div className="card">
        <div className="card-block">
          <h3 className="card-title">{this.state.machine_info.machine_name}</h3>
          <p className="card-text">{this.state.machine_info.machine_sysname}<br/>{this.state.machine_info.machine_mac}<br/></p>
          <Link to={"/machine/"+this.state.machine_info.machine_slug} className="btn btn-primary">
            See details
          </Link>
        </div>
      </div>
    )
  }
}

export default MachineComponent;
