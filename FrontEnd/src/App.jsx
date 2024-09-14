import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

import ShipmentList from "./component/ShipmentList.jsx";
import Header from "./component/Header.jsx";
import Sidebar from "./component/Sidebar.jsx";
import MainContent from "./component/MainContent.jsx";

import "./App.css";

function App() {
  return (
    <>
      {/* 
      
      
      <Footer />
      <BackToTop /> */}
      <MainContent />
      <Header />
      <Sidebar />
      <ShipmentList />
    </>
  );
}

export default App;
