import { useContext } from 'react';
import { Outlet } from 'react-router-dom';
import ServerState, { ServerContext } from './contexts/ServerState';
import useDaemon from './hooks/useDaemon';


function App() {

  const server = useContext(ServerContext)
  
  useDaemon(server)

  return (
    <>
      <ServerState>
        <Outlet />
      </ServerState>
    </>
  );
}

export default App;
