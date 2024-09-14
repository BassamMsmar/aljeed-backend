import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'

// Vendor CSS Files
import './static/assets/vendor/bootstrap/css/bootstrap.min.css';
import './static/assets/vendor/bootstrap-icons/bootstrap-icons.css';
import './static/assets/vendor/boxicons/css/boxicons.min.css';
import './static/assets/vendor/quill/quill.snow.css';
import './static/assets/vendor/quill/quill.bubble.css';
import './static/assets/vendor/remixicon/remixicon.css';
import './static/assets/vendor/simple-datatables/style.css';
import './static/assets/css/style.css';

// // Template Main CSS File
// import './static/assets/css/style.css';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
