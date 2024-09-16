// src/components/Main.jsx
import React from "react";
import ShipmentsTable from "./shipments/ShipmentsTable";
import  Filter from "./shipments/Filter";
import "../styles/Main.css"; // استيراد ملف CSS الخاص بـ Main

const Main = () => {
  return (
    <main className="main">
      
      <Filter />
      <ShipmentsTable />
    </main>
  );
};

export default Main;
