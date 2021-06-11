import axios from "axios";
import { getBaseURL } from "../static/config";
import Qs from "qs";

axios.defaults.baseURL = getBaseURL();
// axios.defaults.headers.post["Content-Type"] =
//   "application/x-www-form-urlencoded";
export async function commonPost(url, load) {
  // let data = {};
  console.log(load);

  const res = await axios.post(url, load).catch((err) => {
    console.log(err);
    return null;
  });
  return res && res.data;
}
