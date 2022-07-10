import { createContext, useContext, useReducer } from 'react'
import { Outlet } from 'react-router-dom'

type Server = {domain: string, port: number, address: string}

type Action = {type: 'connected', payload: Server} | {type: 'disconnected'} | {type: 'failure', payload: any}
type Dispatch = (action: Action) => void
type State = {server: Server, alive: boolean, error: null | any}

const ServerContext = createContext<undefined | {state: State, dispatch: Dispatch}>(undefined)

const serverReducer = (state: State, action: Action):State => {
    switch(action.type) {
        case 'connected': {

            const {domain, port} = action.payload
            const address = `${domain}:${port}`

            const new_state:State = {server: {domain: domain, port: port, address: address}, alive: true, error: null}

            return new_state
        }

        case 'disconnected': {

            const cleared_state: State = {
                server: {domain: "", port: 0, address: ""},
                alive: false,
                error: null
            }

            return cleared_state
        }
        case 'failure': {

            const new_state: State = {
                server: {...state.server},
                alive: false,
                error: action.payload
            }

            return new_state

        }
        default: {
            throw new Error('ServerContext - serverReducer: Action is not recognized.')
        }
    }
}

const ServerProvider = () => {
    const [state, dispatch] = useReducer(serverReducer, {server: {domain: "", port: 0, address: ""}, alive: false, error: null})

    return (
        <ServerContext.Provider value={{state, dispatch}}>
            <Outlet />
        </ServerContext.Provider>
    )
}

const useServerContext = () => {

    const context = useContext(ServerContext)

    if (context === undefined) {
        throw new Error('ServerContext - useServerContext: ServerContext is not within the component tree.')
    }

    return context

}

export {ServerProvider, useServerContext}
