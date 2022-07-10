import { useServerContext } from "../../contexts/ServerContext"
import useReadings from "../../hooks/api/useReadings"

const ReadingsPage = () => {

  const { state } = useServerContext()

  const [loading, data, error] = useReadings(state.server.address)

  return (<>{ JSON.stringify(data) }</>)

}

export default ReadingsPage