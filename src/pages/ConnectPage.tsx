import { useState } from "react"
import { useServerContext } from "../contexts/ServerContext"
import useConnectionCheck from "../hooks/api/useConnectionCheck"
import useConnectionDaemon from "../hooks/api/useConnectionDaemon"

const ConnectPage = () => {

  const {state} = useServerContext()

  const [domain, set_domain] = useState<string>("")
  const [port, set_port] = useState<number>(0)

  const { checkConnection, loading, error } = useConnectionCheck(domain, port)
  const killDaemon = useConnectionDaemon()

  const handleClick = (event: any) => {

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

  return (<>
    { !state.alive ? <>
    <textarea value={domain} onChange={handleDomainInput}  />
    <textarea value={port} onChange={handlePortInput} />
    { state.alive ? `SERVER ALIVE AT ${state.server?.address}` : "SERVER DEAD"}
    <button onClick={handleClick}>Connect Server</button>
    { loading ? "Loading" : "" }
    { error === null ?  "" : `Error Occured - ${error}`}
    { state.error !== null ? `SERVER FAILURE ${state.error.toString()}` : null }
      </>
    : state.alive ? <> <button onClick={handleDisconnectClick}> DISCONENCT</button> </> : null }
  </>)

}

export default ConnectPage