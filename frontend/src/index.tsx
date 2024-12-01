import { ColorModeScript } from "@chakra-ui/react"
import * as React from "react"
import * as ReactDOM from "react-dom/client"
import * as serviceWorker from "./serviceWorker"
import {
  ChakraProvider
} from "@chakra-ui/react"
import { Router } from "./routes";
import "./index.css"
import { theme } from "./utils/theme"

const container = document.getElementById("root")
if (!container) throw new Error('Failed to find the root element');
const root = ReactDOM.createRoot(container)

root.render(
  <React.StrictMode>
    <ColorModeScript />
    <ChakraProvider theme={theme}>
      <Router />
    </ChakraProvider>
  </React.StrictMode>,
)

serviceWorker.unregister()
