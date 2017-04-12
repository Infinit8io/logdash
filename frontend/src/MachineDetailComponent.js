import React, { Component } from 'react'
import './MachineDetail.css'
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
      <div>
        <ol className="breadcrumb">
          <li className="breadcrumb-item"><a href="#">Home</a></li>
          <li className="breadcrumb-item active">State</li>
        </ol>

        <div className="card-columns">
          <HeaderMachineNameBadge machineName="machin" />
          <HeaderSystemNameBadge  systemName="Linux" />
          <HeaderCpuBadge  numCpus="3" />
          <HeaderMemoryBadge memorySize="8" />
        </div>

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
      <h1 className="card-title big-title">{memorySize}</h1>
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
