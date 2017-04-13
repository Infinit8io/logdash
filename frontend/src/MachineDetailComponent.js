import React, { Component } from 'react'
import './MachineDetail.css'
import $ from 'jquery';
import MachineDetailGraphsContainer from './MachineDetailGraphsContainer.js'


  const API_URL = "http://localhost:5000/"

class MachineDetailComponent extends Component {


  constructor(props){
    super(props)
    this.state = {
      machine_info: null,
      machine_data: null,
    }
  }

  componentDidMount(){
    setInterval(() => this.fetchData(),500)
  }

  fetchData(){
    $.get(API_URL+"machine/"+this.props.match.params.id)
      .done(data => this.setState({machine_data: data,machine_info: data[0]}))
      .fail(ex => console.log(ex))
  }

  render(){

    if(this.state.machine_info == null && this.state.machine_data == null)
      return <h1>Loading...</h1>

    return (
      <div>
        <ol className="breadcrumb">
          <li className="breadcrumb-item"><a href="#">Home</a></li>
          <li className="breadcrumb-item active">State</li>
        </ol>

        <div className="card-columns">
          <HeaderMachineNameBadge machineName={this.state.machine_info.machine_name} />
          <HeaderSystemNameBadge  systemName={this.state.machine_info.machine_sysname} />
          <HeaderCpuBadge  numCpus={this.state.machine_info.metrics.cpu.cpu_number_logical} />
          <HeaderMemoryBadge memorySize={this.state.machine_info.metrics.memory.memory_total / 1073741824} />
        </div>

        <MachineDetailGraphsContainer machine_data={this.state.machine_data} />

      </div>
    )
  }
}

const HeaderCpuBadge = ({numCpus}) => (
  <div className="card text-center">
    <div className="card-block">
      <h1 className="card-title big-title">{numCpus}</h1>
      <p className="card-text">cpu(s)</p>
    </div>
  </div>
)

const HeaderMemoryBadge = ({memorySize}) => (
  <div className="card text-center">
    <div className="card-block">
      <h1 className="card-title big-title">{memorySize.toFixed(0)}</h1>
      <p className="card-text">GB of RAM</p>
    </div>
  </div>
)

const HeaderSystemNameBadge = ({systemName}) => (
  <div className="card text-center">
    <div className="card-block">
      <h1 className="card-title big-title">{systemName}</h1>
      <p className="card-text">as the operating system</p>
    </div>
  </div>
)

const HeaderMachineNameBadge = ({machineName}) => (
  <div className="card text-center">
    <div className="card-block">
      <h1 className="card-title big-title">{machineName}</h1>
      <p className="card-text">as the machine name</p>
    </div>
  </div>
)

export default MachineDetailComponent;
