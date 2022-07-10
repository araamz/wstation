import { useState } from 'react';
import { Outlet } from 'react-router-dom';
import { useServerContext } from './contexts/ServerContext';
import useConnectionCheck from './hooks/api/useConnectionCheck';
import useConnectionDaemon from './hooks/api/useConnectionDaemon';

function App() {

  const {state} = useServerContext()

  const [domain, set_domain] = useState<string>("")
  const [port, set_port] = useState<number>(0)

  const { checkConnection, loading, error} = useConnectionCheck(domain, port)
  const killDaemon = useConnectionDaemon()

  const handleConnectClick = (event: any) => {
    event.preventDefault()
    checkConnection()
  }

  const handleDomainInput = (event: any) => {
    event.preventDefault()
    set_domain(event.target.value)
  }

  const handlePortInput = (event: any) => {
    event.preventDefault()
    set_port(event.target.value)
  }

  const handleDisconnectClick = (event: any) => {
    event.preventDefault()
    killDaemon()
  }

  return (
    <>
      {!state.alive ? 
        <div>
          <form>
            <input type="url" value={domain} onChange={handleDomainInput} />
            <input type="number" value={port} onChange={handlePortInput} />
            { !loading ? <input type="submit" value="Connect" onClick={handleConnectClick} /> : null }
          </form>
          { loading ? <div> Loading... </div> : null }
          { error !== null ? <div> There was an error connecting to Device Server. </div> : null }
        </div> 
      : 
        <div>
          <Outlet />
          <nav>
            <button onClick={handleDisconnectClick}>Disconnect</button>
          </nav>
        </div>
      }
    </>
  );
}

export default App;
