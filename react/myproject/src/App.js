// import logo from './logo.svg';
import './App.css';
import ClassComp from './components/ClassComp';
import ConditionalRenComp from './components/ConditionalRenComp';
import FunctionComp from './components/FunctionComp';
import MethodEventComp from './components/MethodEventComp';
import MyDetailsComp from './components/MyDetailsComp';
import MyImagesComp from './components/MyImagesComp';
import ParentComp from './components/ParentComp';
import SetStateComp from './components/SetStateComp';
import ToggleImgComp from './Tasks/ToggleImgComp';

function App() {
  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Hi <code>React</code> App.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
      <h1>Welcome You all in my react session!</h1>
      {/* <FunctionComp myName="Sanjai J" post="Software Developer"/>
      <ClassComp myName="Sanjai J" post="Software Developer"/>
      <MyDetailsComp fname="sanjai" lname="J" email="sanjai2k1j@gmail.com" contact="9176071379" /> */}
      {/* <MethodEventComp/> */}
      {/* <SetStateComp/> */}
      {/* <ConditionalRenComp/> */}
      {/* <MyImagesComp/>

      <ToggleImgComp/> */}
      <ParentComp/>
    </div>
  );
}

export default App;
