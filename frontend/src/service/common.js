import axios from "axios";
import { getBaseURL } from "../static/config";

axios.defaults.baseURL = getBaseURL();

export function commonPost(url, load) {
  let data = {};
  axios
    .post(url, load)
    .catch((err) => {
      console.log(err);
    })
    .then((response) => {
      data = response.data;
    })
    .catch((err) => {
      console.log(err);
    });
  return data;
}
