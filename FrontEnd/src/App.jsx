import {BrowserRouter,Routes, Route} from 'react-router-dom';
import {Home} from './pages/home';
import {Investigadores} from './pages/investigadores';
import {Navigation} from './components/navigation';
import { InvestigadoresFormPage } from './pages/investigadoresFormPage';
import {Toaster} from 'react-hot-toast';
import React from "react";


function App() {
  return (
    
    <BrowserRouter>

      <Navigation />
      <div className='ml-82'>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/home" element={<Home />} />
          <Route path="/investigadores" element={<Investigadores />} />
          <Route path="/investigadoresFormPage" element={<InvestigadoresFormPage />} />
          {/* <Route path="/investigadoresDet" element={<InvestigadoresDet />} /> */}
        </Routes>
        <Toaster />
      </div>

    </BrowserRouter>
  )
}

export default App