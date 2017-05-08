import React, { Component } from 'react'
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'

import Chart from 'chart.js'

export default class MachineDetailCpuGraph extends Component {

  componentDidMount(){

    let canvas = document.getElementById("cpu-chart")
    let ctx = canvas.getContext('2d')
    this.setState({
      canvas: canvas,
      ctx:ctx,
      chart: new Chart(ctx , {
          type: "line",
          data: this.state.graphData,
          scales: {
            yAxes: [{
              type: "user-defined",
              ticks: {
                beginAtZero: true,
                min: 0,
                max: 100,
                fixedStepSize: 10,
              }
            }]
        }
      })
    })
  }

   componentWillReceiveProps(nextProps){

      let newData = nextProps.machine_data.filter(data => data.metrics_took_at > this.state.lastTimeStamp)

      if(newData.length > 0){
        let chart = this.state.chart

        chart.data.datasets.forEach((set, index) => {

          //Remove old data
          set.data.shift()

          set.data.push(...newData.map(data => {
            return data.metrics.cpu.cpu_per_cpu_percentage[index]
          }))

        })

        newData.forEach(data => {
          chart.data.labels.shift()
          let date = new Date(data.metrics_took_at * 1000)
          chart.data.labels.push(date.getHours()+" : "+date.getMinutes() + " : " +date.getSeconds())
        })

        let ts = Math.max(...newData.map(d => d.metrics_took_at))
        console.log(ts)
        this.setState({lastTimeStamp: ts})
        chart.update()
      }
   }
  createDataSets(machine_data){
    //If someone finds a nice functionnal way to do this, I will give him a cookie

    let cpuCount = machine_data[0].metrics.cpu.cpu_number_logical;
    let _datasets = []

    for(let index=0;index < cpuCount; index++){

      _datasets.push(
        {
          label: 'CPU '+ index,
          fill: false,
          lineTension: 0.2,
          backgroundColor: this.cpuColors[index].color1,
          borderColor: this.cpuColors[index].color2,
          borderCapStyle: 'butt',
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: 'miter',
          pointBorderColor: this.cpuColors[index].color2,
          pointBackgroundColor: '#fff',
          pointBorderWidth: 1,
          pointHoverRadius: 2,
          pointHoverBackgroundColor: this.cpuColors[index].color2,
          pointHoverBorderColor: this.cpuColors[index].color3,
          pointHoverBorderWidth: 1,
          pointRadius: 1,
          pointHitRadius: 10,
          data: machine_data.map(data => data.metrics.cpu.cpu_per_cpu_percentage[index])
        }
      )
    }
    return _datasets
  }
  constructor(props){
    super(props)

    this.cpuColors = this.props.machine_data[0].metrics.cpu.cpu_per_cpu_percentage.map(cpu => {
        return {
        color1 : this.getRandomColor(),
        color2 : this.getRandomColor(),
        color3 : this.getRandomColor(),
      }
    })

    this.state = {
      graphData: {
        labels: this.props.machine_data.map(data => {
          //Not sure if this is efficient
          let date = new Date(data.metrics_took_at * 1000)
          return date.getHours()+" : "+date.getMinutes() + " : " +date.getSeconds()
        }),
        datasets: this.createDataSets(this.props.machine_data)
      },
      lastTimeStamp: Math.max(...this.props.machine_data.map(d => d.metrics_took_at))
    }
  }

  getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  render(){
    return (
      <canvas id="cpu-chart">
      </canvas>
    )
  }

}
