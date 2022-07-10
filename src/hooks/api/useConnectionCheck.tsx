import { useCallback, useState } from "react"
import { useServerContext } from "../../contexts/ServerContext"
const useConnectionCheck = (domain: string, port: number) => {

    const {dispatch} = useServerContext()

    const [loading, set_loading] = useState<boolean>(false)
    const [error, set_error] = useState<any>(null)

    const checkConnection = useCallback(() => {

        set_loading(true)
        set_error(null)
  
        fetch(`${domain}:${port}/device/alive`)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Sever Offline")
          }

          dispatch({
            type:'connected', 
            payload: {domain: domain, port: port, address: ""}
          })

        }).catch((error) => {
        dispatch({
            type:'disconnected', 
        })
            set_error(error)
        })
  
        set_loading(false)
  
    }, [port, domain, dispatch]) 


    return { checkConnection, loading, error}

}

export default useConnectionCheck;