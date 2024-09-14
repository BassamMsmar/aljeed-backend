// src/main.jsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import 'bootstrap/dist/css/bootstrap.min.css';
import App from "./App.jsx";
import "./styles/App.css"; // استيراد ملف CSS الرئيسي

const root = createRoot(document.getElementById("root"));
root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
