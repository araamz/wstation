import useFetch from "../useFetch"

const useReadings = (server: string) => {

    let {loading, data, error} = useFetch(`${server}/readings/`)

    return [loading, data, error]

}

export default useReadings