import React, { Component } from 'react';
import logo from './logo.svg';
import MachineContainer from './MachineContainer.js'
import MachineDetailComponent from './MachineDetailComponent.js'

import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'


class App extends Component {
  render() {
    return (
      <Router>
          <div>
            <Route exact path="/" component={MachineContainer}/>
            <Route excat path="/machine/:id" component={MachineDetailComponent}/>
          </div>
      </Router>
    );
  }
}

export default App;
