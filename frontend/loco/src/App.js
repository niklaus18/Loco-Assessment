import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import ListTransaction from "./component/user/ListTransaction";
import './App.css';

function App() {
  return (
    <div className="App">
      <Router>
        <div className="col-md-6">
          <h1 className="text-center" style={style}>Transaction Application (Loco Assignment)</h1>
          <ListTransaction/>
        </div>
      </Router>
    </div>
  );
}

const style = {
  color: 'black',
  margin: '10px'
}

export default App;
