import { useCallback, useEffect, useState } from "react";

const useFetch = (url:string) => {

    const [loading, set_loading] = useState<boolean>(true)
    const [data, set_data] = useState<any>()
    const [error, set_error] = useState<any>(null)

    const refetchRequest = useCallback(async () => {

        try {
            const request:Response = await fetch(url)
            const request_data:JSON = await request.json()

            if (!request.ok) {
                throw Error(`ERROR: ${request.statusText} - ${request.status}`)
            }
            console.log(request_data)
            set_data(request_data)
            set_error(null)
        } catch (error) {
            set_error(error)
        } finally {
            set_loading(false)
        }
        
        return

    }, [url])

    useEffect(() => {

        let abort_controller:AbortController = new AbortController()

        const fetchData = async (abort_controller:AbortController) => {
            
            try {
                const request:Response = await fetch(url, {signal: abort_controller.signal})
                const request_data:JSON = await request.json()
        
                if (!request.ok) {
                    throw Error(`ERROR: ${request.statusText} - ${request.status}`)
                }
                set_data(request_data)
            } catch (error) {
                if (!abort_controller.signal.aborted) { 
                    set_error(error)
                }
            } finally {
                set_loading(false)
            }

        }

        fetchData(abort_controller)

        return () => {
            abort_controller.abort()
        }

    }, [url])


    return {loading, data, error, refetchRequest}

}

export default useFetch;