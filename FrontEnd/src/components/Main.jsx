// src/components/Main.jsx
import React from 'react';
import ShipmentsTable from './ShipmentsTable';
import '../styles/Main.css'; // استيراد ملف CSS الخاص بـ Main

const Main = () => {
  return (
    <main className="main">
      <h2>Welcome to the Dashboard</h2>
      <ShipmentsTable />
    </main>
  );
};

export default Main;
