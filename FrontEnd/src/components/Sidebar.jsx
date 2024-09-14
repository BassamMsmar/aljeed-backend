// src/components/Sidebar.jsx
import React from 'react';
import '../styles/Sidebar.css'; // استيراد ملف CSS الخاص بـ Sidebar

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <nav>
        <ul>
          <li><a href="#">Dashboard</a></li>
          <li><a href="#">Profile</a></li>
          <li><a href="#">Messages</a></li>
          <li><a href="#">Settings</a></li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
