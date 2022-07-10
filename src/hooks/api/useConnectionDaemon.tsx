import { useCallback, useEffect } from "react";
import { useServerContext } from "../../contexts/ServerContext";

const useConnectionDaemon = () => {

    const {state, dispatch} = useServerContext()

    useEffect(() => {

        let periodicUpdate:any = null

        if (state.alive) {
            periodicUpdate = setInterval(() => {

                console.log("Checking at " + state.server.address)

                fetch(`${state.server?.address}/device/alive`).then((response) => {
                    if (!response.ok) {
                        throw new Error('Server Disconnected')
                    }
                }).catch((error) => {
                    
                    dispatch({type: 'failure', payload: error})

                })

            }, 5000)
        }

        return () => {
            clearInterval(periodicUpdate)
        }

    }, [state.alive, dispatch, state.server?.address])


    const killDaemon = useCallback(() => {

        dispatch({type: 'disconnected'})

    }, [dispatch])

    return killDaemon
    
    
}

export default useConnectionDaemon;