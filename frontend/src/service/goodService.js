import axios from "axios";
import { getBaseURL } from "../static/config";

axios.defaults.baseURL = getBaseURL();
