import React, { Component } from 'react'
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'


import MachineDetailCpuGraph from './MachineCpuDetailGraph.js'
import MachineDetailMemoryGraph from './MachineMemoryDetailGraph.js'

class MachineDetailGraphsContainer extends Component {

  constructor(props){
    super(props)
    this.state = {
      machine_data : props.machine_data
    }
  }

  componentDidMount(){
  }

  componentWillReceiveProps(nextProps){
    this.setState({machine_data: nextProps.machine_data})
  }

  render(){
    if(this.state.machine_data != null){
      return  (
        <div>
        <ul className="nav nav-pills nav-fill" role="tablist">
          <li className="nav-item">
            <a className="nav-link active" role="tab" data-toggle="tab" href="#cpu">CPU</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" role="tab" data-toggle="tab" href="#memory">Memory</a>
          </li>

        </ul>
          <div className="card-block">
            <div className="tab-content">
              <div className="tab-pane active" id="cpu" role="tabpanel">
                <MachineDetailCpuGraph machine_data={this.state.machine_data}/>
              </div>
              <div className="tab-pane" id="memory" role="tabpanel">
                <MachineDetailMemoryGraph machine_data={this.state.machine_data}/>
              </div>
            </div>
          </div>
        </div>
      )
    }else{
      return <div>No data</div>
    }
  }
}



export default MachineDetailGraphsContainer
