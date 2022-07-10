import { useServerContext } from "../../contexts/ServerContext"
import useLiveReading from "../../hooks/api/useLiveReading"

const LivePage = () => {

    const { state } = useServerContext()

    const [loading, data, error] = useLiveReading(state.server.address)

    return <>{JSON.stringify(data)}</>

}
export default LivePage