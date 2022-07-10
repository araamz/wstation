import { useEffect } from "react"
import useFetch from "../useFetch"

const useLiveReading = (server: string) => {

    let {loading, data, error, refetchRequest} = useFetch(`${server}/device/live/reading`)

    useEffect(() => {

        const periodicUpdate = setInterval(() => {
            refetchRequest()
        }, 2000)

        return () => {
            clearInterval(periodicUpdate)
        }

    }, [refetchRequest])

    return [loading, data, error]

}

export default useLiveReading