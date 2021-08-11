import React from 'react';
// import logo from './logo.svg';
// import './App.css';
import { Route } from 'react-router-dom';
import HomePage from './components/pages/Home';
import LoginPage from './components/pages/Login';
import RegisterPage from './components/pages/Register';

// function App() {
//     return (
//         <div className="App">
//             <header className="App-header">
//                 <img src={logo} className="App-logo" alt="logo" />
//                 <p>
//                     Edit <code>src/App.tsx</code> and save to reload.
//                 </p>
//                 <a className="App-link" href="https://reactjs.org" target="_blank" rel="noopener noreferrer">
//                     Learn React
//                 </a>
//             </header>
//         </div>
//     );
// }
function App() {
    return (
        <>
            <Route exact path="/" component={HomePage} />
            <Route path="/login" component={LoginPage} />
            <Route path="/register" component={RegisterPage} />
        </>
    );
}

export default App;
