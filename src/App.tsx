import { Outlet } from 'react-router-dom';
import { ServerProvider } from './contexts/ServerContext';

function App() {


  return (
    <ServerProvider>
      <p>
        Testing
      </p>
      <Outlet />
    </ServerProvider>
  );
}

export default App;
