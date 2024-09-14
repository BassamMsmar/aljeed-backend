// src/components/App.jsx
import React from 'react';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Main from './components/Main';
import './styles/App.css'; // استيراد ملف CSS الرئيسي

const App = () => {
  return (
    <div className="app">
      <Header />
      <div className="container">
        <Sidebar />
        <Main />
      </div>
    </div>
  );
};

export default App;
